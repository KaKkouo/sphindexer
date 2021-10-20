"""
Sphindexer
~~~~~~~~~~
A Sphinx Indexer.
:copyright: Copyright 2021 by @KoKekkoh.
:license: BSD, see LICENSE for details.
"""

__copyright__ = 'Copyright (C) 2021 @koKekkoh'
__license__ = 'BSD 2-Clause License'
__author__  = '@koKekkoh'
__version__ = '0.1.1' # 2021-10-21
__url__     = 'https://github.com/KaKkouo/sphindexer'

import re, pathlib
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Pattern, Type, cast

from docutils import nodes

import sphinx.builders.html as builders
from sphinx.domains.index import IndexDomain
from sphinx.errors import NoUri
from sphinx.environment.adapters.indexentries import IndexEntries
from sphinx.locale import _, __
from sphinx.util import logging
from sphinx.util.nodes import process_index_entry
from sphinx.writers import html5

logger = logging.getLogger(__name__)

#------------------------------------------------------------

class Text(nodes.Text):
    def __init__(self, rawword):
        self.textclass = Text
        self._rawword = rawword
        super().__init__(rawword, rawword)

#------------------------------------------------------------

_each_words = re.compile(r' *; +')

class IndexEntry(nodes.Element):

    def __init__(self, rawtext, entry_type='single',
                 file_name=None, target=None, main='', index_key='', textclass=Text):
        """
        - textclass: to expand functionality for multi-byte language.
        """

        self.delimiter = '; '
        self.textclass = textclass

        rawwords = _each_words.split(rawtext)

        terms = []
        for rawword in rawwords:
            terms.append(textclass(rawword))

        super().__init__(rawtext, *terms, entry_type=entry_type, 
                         file_name=file_name, target=target, main=main, index_key=index_key)

    def __repr__(self):
        """
        >>> tentry = IndexEntry('sphinx; python', 'single', 'document', 'term-1')
        >>> tentry
        <IndexEntry: entry_type='single' file_name='document' target='term-1' <#text: 'sphinx'><#text: 'python'>>
        """

        name = self.__class__.__name__
        prop = f"<{name}: "

        etype, ikey = self['entry_type'], self['index_key']
        main, fn, tid = self['main'], self['file_name'], self['target']

        if etype: prop += f"entry_type='{etype}' "
        if main:  prop += f"main='{main}' "
        if fn:    prop += f"file_name='{fn}' "
        if tid:   prop += f"target='{tid}' "
        if ikey:  prop += f"index_key='{ikey}' "

        children = ''.join([repr(c) for c in self])
        prop += children + ">"

        return prop

    def astext(self):
        """
        >>> tentry = IndexEntry('sphinx; python', 'single', 'document', 'term-1', None)
        >>> tentry.astext()
        'sphinx; python'
        """
        delimiter = self.delimiter
        text = delimiter.join(k.astext() for k in self)
        return text

    def make_index_units(self):
        """
        >>> tentry = IndexEntry('sphinx', 'single', 'document', 'term-1')
        >>> tentry.make_index_units()
        [<IndexUnit: main='5' file_name='document' target='term-1' <#text: ''><#text: 'sphinx'>>]
        """
        etype = self['entry_type']
        fn = self['file_name']
        tid = self['target']
        main = self['main']
        index_key = self['index_key']

        def _index_unit(term, sub1, sub2):
            if etype in ('see', 'seealso'):
                emphasis = _emphasis2char[etype]
            else:
                emphasis = _emphasis2char[main]

            if not sub1: sub1 = term.textclass('')
            if not sub2: sub2 = term.textclass('')

            index_unit = IndexUnit(term, sub1, sub2, emphasis, fn, tid, index_key)
            return index_unit

        index_units = []
        try:
            #_index_unit(term, subterm1, subterm2)
            if etype == 'single':
                try:
                    index_units.append(_index_unit(self[0], self[1], ''))
                except IndexError:
                    index_units.append(_index_unit(self[0], '', ''))
            elif etype == 'pair':
                index_units.append(_index_unit(self[0], self[1], ''))
                index_units.append(_index_unit(self[1], self[0], ''))
            elif etype == 'triple':
                index_units.append(_index_unit(self[0], self[1], self[2]))
                u = _index_unit(self[1], self[2], self[0])
                u.set_subterm_delimiter()
                index_units.append(u)
                index_units.append(_index_unit(self[2], self[0], self[1]))
            elif etype == 'see':
                index_units.append(_index_unit(self[0], self[1], ''))
            elif etype == 'seealso':
                index_units.append(_index_unit(self[0], self[1], ''))
            elif etype in self._number_of_terms:
                for i in range(len(self)):
                    index_units.append(_index_unit(self[i], '', ''))
            else:
                logger.warning(__('unknown index entry type %r'), etype,
                                  location=fn)
        except ValueError as err:
            logger.warning(str(err), location=fn)

        return index_units

#------------------------------------------------------------

#1-5: IndexRack.put_in_kana_catalogでの優先順.
#3,5: 同一term/subterm内でのリンクの表示順.
#8,9: 便宜上ここに割り当てる. 表示順は別途.
_emphasis2char = {
    '_rsvd0_': '0', #reserved
    '_rsvd1_': '1', #reserved
    '_rsvd2_': '2', #reserved
    'main':    '3', #glossaryで定義した用語. indexでは「!」が先頭にあるもの.
    '_rsvd4_': '4', #reserved
    '':        '5', #'main', 'see', 'seealso'以外.
    '_rsvd6_': '6', #reserved
    '_rsvd7_': '7', #reserved
    'see':     '8',
    'seealso': '9',
}

_char2emphasis = {
    '0': '', '1': '', '2': '', '3': 'main', '4': '',
    '5': '', '6': '', '7': '', '8': 'see', '9': 'seealso',
}

def make_classifier_from_first_letter(text):
    return text[:1].upper()

class IndexRack(object):
    """
    1. self.__init__() 初期化. 設定からの読み込み.
    2. self.append() IndexUnitの取り込み. self.update()の準備.
    3. self.update_units() 各unitの更新、並び替えの準備.
    4. self.sort_units() 並び替え.
    5. self.generate_genindex_data() genindex用データの生成.
    """
    
    UNIT_CLSF, UNIT_TERM, UNIT_SBTM, UNIT_EMPH = 0, 1, 2, 3

    def __init__(self, builder):
        """IndexUnitの取り込み、整理、並べ替え. データの生成."""

        #制御情報の保存
        self.env = builder.env
        self.config = builder.config
        self.get_relative_uri = builder.get_relative_uri

    def create_genindex(self, group_entries: bool = True,
                       _fixre: Pattern = re.compile(r'(.*) ([(][^()]*[)])')
                     ) -> List[Tuple[str, List[Tuple[str, Any]]]]:
        """IndexEntriesクラス/create_indexメソッドを置き換える."""

        #引数の保存
        self._group_entries = group_entries
        self._fixre = _fixre

        #入れ物の用意とリセット
        self._rack = [] # [IndexUnit, IndexUnit, ...]
        self._classifier_catalog = {} # {term: classifier} 
        self._function_catalog = {} #{function name: number of homonymous funcion}

        domain = cast(IndexDomain, self.env.get_domain('index'))
        entries = domain.entries
        #entries: Dict{ファイル名: List[Tuple(type, value, tid, main, index_key)]}

        for fn, entries in entries.items():
            for entry_type, value, tid, main, index_key in entries:
                unit = IndexEntry(value, entry_type, fn, tid, main, index_key)
                index_units = unit.make_index_units()
                self.extend(index_units)

        self.update_units()
        self.sort_units()

        return self.generate_genindex_data() 

    def append(self, unit):
        """
        - 全unitを見て決める更新処理のための情報収集
        """
        #情報収集
        self.put_in_classifier_catalog(unit['index_key'], unit[self.UNIT_TERM].astext())

        #情報収集
        if self._group_entries:
            self.put_in_function_catalog(unit.astexts(), self._fixre)

        #unitをrackに乗せる
        self._rack.append(unit)

    def extend(self, units):
        for unit in units:
            self.append(unit)

    def put_in_classifier_catalog(self, index_key, hier):
        """Text/KanaText共通の処理"""
        if not index_key: return
        if not hier: return

        if not hier in self._classifier_catalog:
            #上書きはしない.（∵「make clean」での状況を真とするため）
            self._classifier_catalog[hier] = index_key

    def put_in_function_catalog(self, texts, _fixre):
        for text in texts:
            m = _fixre.match(text)
            if m:
                try:
                    self._function_catalog[m.group(1)] += 1
                except KeyError:
                    self._function_catalog[m.group(1)] = 1
            else:
                pass

    def update_units(self):
        """rackに格納されている全てのunitの更新を行う."""

        #カタログ情報を使った更新
        for unit in self._rack:
            assert [unit[self.UNIT_TERM]]

            #複数ある同名関数の更新

            if self._group_entries:
                self.update_unit_with_function_catalog(unit)

            #classifierの設定

            ikey = unit['index_key']
            term = unit[self.UNIT_TERM]

            #［重要］if/elifの判定順
            if ikey:
                unit[self.UNIT_CLSF] = term.textclass(ikey)
            elif term.astext() in self._classifier_catalog:
                unit[self.UNIT_CLSF] = term.textclass(self._classifier_catalog[term.astext()])
            else:
                text = unit[self.UNIT_TERM].astext()
                char = make_classifier_from_first_letter(text)
                unit[self.UNIT_CLSF] = term.textclass(char)

            #sortkeyの設定
            #'see', 'seealso'の表示順に手を加える.

            if unit[self.UNIT_EMPH] in ('7', '8', '9'):
                order_code = '1' #'see' or 'seealso'
            else:
                order_code = '2' #'main' or ''

            unit._sort_order = order_code

    def update_unit_with_function_catalog(self, unit):
        """
        fixup entries: transform
          func() (in module foo)
          func() (in module bar)
        into
          func()
            (in module foo)
            (in module bar) 
        """
        i_tm = unit[self.UNIT_TERM]
        m = self._fixre.match(i_tm.astext())

        #_fixreが想定する形で関数名とモジュール名があり、同じ名前の関数が複数ある場合.
        if m and self._function_catalog[m.group(1)] > 1:
            #状況的にsubtermは空のはず.
            assert not unit[self.UNIT_SBTM], f'{self.__class__.__name__}: subterm is not null'

            unit[self.UNIT_TERM] = i_tm.textclass(m.group(1))
            obj = i_tm.textclass(m.group(2))
            unit[self.UNIT_SBTM] = SubTerm()
            unit[self.UNIT_SBTM].append(obj)
        #subの情報が消えるが、このケースに該当する場合はsubにはデータがないはず.

    def sort_units(self):
        self._rack.sort(key=lambda x: (
            x[self.UNIT_CLSF].astext(), #classifier
            x[self.UNIT_TERM].astext(), #term
            x._sort_order,              #entry type in('see', 'seealso')
            x[self.UNIT_SBTM].astext(), #subterm
            x[self.UNIT_EMPH],          #emphasis(main)
            x['file_name'], x['target']))
        #x['file_name'], x['target']について.
        #逆にすると内部的な処理順に依存するため、現状の動作仕様を維持する.

    def generate_genindex_data(self):
        """
        Text/KanaTextの選択を意識して書く.
        （Text側で__eq__が実装されることが前提）
        """
        rtnlist = [] #判定用

        _clf, _tm, _sub = -1, -1, -1
        for unit in self._rack: #rackからunitを取り出す
            i_clf = unit[self.UNIT_CLSF]
            i_tm  = unit[self.UNIT_TERM]
            i_sub = unit[self.UNIT_SBTM] #see: SubTerm
            i_em  = unit[self.UNIT_EMPH]
            i_fn  = unit['file_name']
            i_tid = unit['target']
            i_iky = unit['index_key']

            #make a uri
            if i_fn:
                try:
                    r_uri = self.get_relative_uri('genindex', i_fn) + '#' + i_tid
                except NoUri:
                    continue

            #see: KanaText.__ne__
            if len(rtnlist) == 0 or not rtnlist[_clf][0] == i_clf.astext(): 
                rtnlist.append((i_clf, []))

                #追加された「(clf, [])」を見るように_clfを更新する. 他はリセット.
                _clf, _tm, _sub = _clf+1, -1, -1

            r_clsfr = rtnlist[_clf] #[classifier, [term, term, ..]]
            r_clfnm = r_clsfr[0] #classifier is KanaText object.
            r_subterms = r_clsfr[1] #[term, term, ..]

            #see: KanaText.__ne__
            if len(r_subterms) == 0 or not r_subterms[_tm][0] == i_tm.astext(): #use __eq__
                r_subterms.append((i_tm, [[], [], i_iky]))

                #追加された「(i_tm, [[], [], i_iky])」を見るように_tmを更新する. _subはリセット.
                _tm, _sub = _tm+1, -1

            r_term = r_subterms[_tm]    #[term, [links, [subterm, subterm, ..], index_key]
            r_term_value = r_term[0]    #term_value is KanaText object.
            r_term_links = r_term[1][0] #[(main, uri), (main, uri), ..]
            r_subterms = r_term[1][1]   #[subterm, subterm, ..]

            #一文字から元の文字列に戻す
            r_main = _char2emphasis[i_em]

            #see/seealsoならリンク情報を消す
            if r_main in ('see', 'seealso'):
                r_fn = None
            else:
                r_fn = i_fn
                
            #sub(class SubTerm): [], [KanaText], [KanaText, KanaText].
            if len(i_sub) == 0:
                if r_fn: r_term_links.append((r_main, r_uri))
            elif len(r_subterms) == 0 or not r_subterms[_sub][0] == i_sub.astext():
                r_subterms.append((i_sub, []))

                _sub = _sub+1
                r_subterm = r_subterms[_sub]
                r_subterm_value = r_subterm[0]
                r_subterm_links = r_subterm[1]
                if r_fn: r_subterm_links.append((r_main, r_uri))
            else:
                if r_fn: r_subterm_links.append((r_main, r_uri))

        return rtnlist

class SubTerm(nodes.reprunicode):
    """
    """
    def __init__(self, template=None):
        self._terms = []
        self._delimiter = ' '
        self._template = template
    def set_delimiter(self, delimiter):
        self._delimiter = delimiter
    def __repr__(self):
        rpr  = f"<{self.__class__.__name__}: len={len(self)} "
        if self._template: rpr += f"tpl='{self._template}' "
        for s in self._terms:
            rpr += repr(s)
        rpr += ">"
        return rpr
    def __str__(self):
        """Jinja2"""
        return self.astext()
    def __eq__(self, other):
        """unittest、IndexRack.generate_genindex_data."""
        return self.astext() == other
    def __len__(self):
        return len(self._terms)
    def append(self, subterm):
        self._terms.append(subterm)
    def astext(self):
        if self._template and len(self) == 1:
            return self._template % self._terms[0].astext()

        text = ""
        for subterm in self._terms:
            text += subterm.astext() + self._delimiter
        return text[:-len(self._delimiter)]

class IndexUnit(object):

    CLSF, TERM, SBTM, EMPH = 0, 1, 2, 3

    def __init__(self, term, subterm1, subterm2, emphasis, file_name, target, index_key):

        if emphasis == '8':
            subterm = SubTerm(_('see %s'))
        elif emphasis == '9':
            subterm = SubTerm(_('see also %s'))
        else:
            subterm = SubTerm()

        for sbtm in (subterm1, subterm2):
            if sbtm.astext():
                subterm.append(sbtm)

        self._display_data = [term.textclass(''), term, subterm]
        self._link_data = (emphasis, file_name, target)
        self._index_key = index_key

    def __repr__(self):
        """
        """
        name = self.__class__.__name__
        main = self['main']
        fn = self['file_name']
        tid = self['target']
        rpr  = f"<{name}: "
        if main: rpr += f"main='{main}' "
        if fn: rpr += f"file_name='{fn}' "
        if tid: rpr += f"target='{tid}' "
        rpr += repr(self[0]) + repr(self[1])
        if len(self[2]) > 0: rpr += repr(self[2])
        rpr += ">"
        return rpr

    def __getitem__(self, key):
        if isinstance(key, str):
            if key == 'main':      return self._link_data[0]
            if key == 'file_name': return self._link_data[1]
            if key == 'target':    return self._link_data[2]
            if key == 'index_key': return self._index_key
            raise KeyError(key)
        elif isinstance(key, int):
            if key == self.CLSF: return self._display_data[self.CLSF] #classifier
            if key == self.TERM: return self._display_data[self.TERM] #term
            if key == self.SBTM: return self._display_data[self.SBTM] #subterm
            if key == self.EMPH: return self._link_data[0]    #emphasis(main)
            raise KeyError(key)
        else:
            raise TypeError(key)

    def __setitem__(self, key, value): #更新するデータだけ対応する.
        if isinstance(key, int):
            if key == self.CLSF: self._display_data[self.CLSF] = value
            elif key == self.TERM: self._display_data[self.TERM] = value
            elif key == self.SBTM: self._display_data[self.SBTM] = value
            elif key == self.EMPH: self._display_data[self.EMPH] = value
            else: raise KeyError(key)
        else:
            raise KeyError(key)

    def get_children(self):
        children = [self[self.TERM]]
        if self[2]:
            for child in self[self.SBTM]._terms:
                children.append(child)
        return children

    def set_subterm_delimiter(self, delimiter=', '):
        self[self.SBTM].set_delimiter(delimiter)

    def astexts(self):
        texts = [self[self.TERM].astext()]

        for subterm in self[self.SBTM]._terms:
            texts.append(subterm.astext())

        return texts

#------------------------------------------------------------

class _StandaloneHTMLBuilder(builders.StandaloneHTMLBuilder):

    def index_adapter(self) -> None: #KaKkou
        return IndexEntries(self.env).create_index(self)

    def write_genindex(self) -> None:
        genindex = self.index_adapter()

        #以降の処理はSphinx4.1.2オリジナルと同じ
        indexcounts = []
        for _k, entries in genindex:
            indexcounts.append(sum(1 + len(subitems)
                                   for _, (_, subitems, _) in entries))

        genindexcontext = {
            'genindexentries': genindex,
            'genindexcounts': indexcounts,
            'split_index': self.config.html_split_index,
        }
        logger.info('genindex ', nonl=True)

        if self.config.html_split_index:
            self.handle_page('genindex', genindexcontext,
                             'genindex-split.html')
            self.handle_page('genindex-all', genindexcontext,
                             'genindex.html')
            for (key, entries), count in zip(genindex, indexcounts):
                ctx = {'key': key, 'entries': entries, 'count': count,
                       'genindexentries': genindex}
                self.handle_page('genindex-' + key, ctx,
                                 'genindex-single.html')
        else:
            self.handle_page('genindex', genindexcontext, 'genindex.html')

class HTMLBuilder(_StandaloneHTMLBuilder):
    """索引ページの日本語対応"""

    name = 'idxr'

    def dispatch_indexer(self) -> None: #KaKkou
        """索引の作成"""

        #自前のIndexerを使う
        return IndexRack(self).create_genindex()

#------------------------------------------------------------

def setup(app) -> Dict[str, Any]:
    """各クラスや設定の登録

    :param app: add_buidder, add_config_valueの実行に必要
    :type app: Sphinx
    :return: 本Sphinx拡張の基本情報など
    :rtype: Dict[name: value]
    """

    app.add_builder(HTMLBuilder)

    return {
            'version': __version__,
            'parallel_read_safe': True,
            'parallel_write_safe': True,
        }

#------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    doctest.testmod()
