"""
Sphindexer
~~~~~~~~~~
A Sphinx Indexer.

:copyright: Copyright 2021 by @koKekkoh.
:license: BSD, see LICENSE for details.
"""

from typing import Any, Dict, List, Tuple

from docutils import nodes

from sphinx import addnodes
from sphinx.builders import html as builders
from sphinx.domains.index import IndexRole
from sphinx.util import logging
from sphinx.util.nodes import process_index_entry

from . import rack

__copyright__ = 'Copyright (C) 2021 @koKekkoh'
__license__   = 'BSD 2-Clause License'
__author__    = '@koKekkoh'
__version__   = '0.5.4.1'  # 2021-10-29
__url__       = 'https://github.com/KaKkouo/sphindexer'

logger = logging.getLogger(__name__)

# ------------------------------------------------------------


class Subterm(rack.Subterm): pass
class IndexUnit(rack.IndexUnit): pass
class IndexEntry(rack.IndexEntry): pass
class IndexRack(rack.IndexRack): pass


# ------------------------------------------------------------

class XRefIndex(IndexRole):
    """
    based on
    https://github.com/sphinx-doc/sphinx/blob/4.x/sphinx/domains/index.py
    """

    def textclass(sefl, text, rawtext):
        return nodes.Text(text, rawtext)

    def run(self) -> Tuple[List[nodes.Node], List[nodes.system_message]]:
        target_id = 'index-%s' % self.env.new_serialno('index')
        if self.has_explicit_title:
            # if an explicit target is given, process it as a full entry
            title = self.title
            entries = process_index_entry(self.target, target_id)
        else:
            # otherwise we just create a single entry
            if self.target.startswith('!'):
                title = self.title[1:]
                entries = [('single', self.target[1:], target_id, 'main', None)]
            else:
                title = self.title
                entries = [('single', self.target, target_id, '', None)]

        index = addnodes.index(entries=entries)
        target = nodes.target('', '', ids=[target_id])
        text = self.textclass(title, title)
        self.set_source_info(index)
        return [index, target, text], []


# ------------------------------------------------------------


class _StandaloneHTMLBuilder(builders.StandaloneHTMLBuilder):
    """
    based on
    https://github.com/sphinx-doc/sphinx/blob/4.x/sphinx/builders/html/__init__.py
    """

    def index_adapter(self) -> None:
        raise NotImplementedError

    def write_genindex(self) -> None:
        genindex = self.index_adapter()

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

    name = 'idxr'

    def index_adapter(self) -> None:
        return IndexRack(self).create_index()


# ------------------------------------------------------------


def setup(app) -> Dict[str, Any]:

    app.add_builder(HTMLBuilder)

    return {'version': __version__,
            'parallel_read_safe': True,
            'parallel_write_safe': True,
            }


# ------------------------------------------------------------


if __name__ == '__main__':
    import doctest
    doctest.testmod()
