"""
made by the std.py of Sphinx4.4.0
"""
import re
import warnings
from copy import copy
from typing import (TYPE_CHECKING, Any, Callable, Dict, Iterable, Iterator, List, Optional,
                    Tuple, Type, Union, cast)

from docutils import nodes
from docutils.nodes import Element, Node, system_message
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList

from sphinx import addnodes
from sphinx.addnodes import desc_signature, pending_xref
from sphinx.deprecation import RemovedInSphinx50Warning
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, ObjType
from sphinx.locale import _, __
from sphinx.roles import XRefRole
from sphinx.util import docname_join, logging, ws_re
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import clean_astext, make_id, make_refnode
from sphinx.util.typing import OptionSpec, RoleFunction

from sphinx.domains.std import StandardDomain


def split_term_classifiers(line: str) -> List[Optional[str]]:
    # split line into a term and classifiers. if no classifier, None is used..
    parts: List[Optional[str]] = re.split(' +: +', line) + [None]
    return parts


def make_glossary_term(env: "BuildEnvironment", textnodes: Iterable[Node], index_key: str,
                       source: str, lineno: int, node_id: str, document: nodes.document
                       ) -> nodes.term:
    # get a text-only representation of the term and register it
    # as a cross-reference target
    term = nodes.term('', '', *textnodes)
    term.source = source
    term.line = lineno
    termtext = term.astext()

    if node_id:
        # node_id is given from outside (mainly i18n module), use it forcedly
        term['ids'].append(node_id)
    else:
        node_id = make_id(env, document, 'term', termtext)
        term['ids'].append(node_id)
        document.note_explicit_target(term)

    std = cast(StandardDomain, env.get_domain('std'))
    std._note_term(termtext, node_id, location=term)

    # add an index entry too
    indexnode = addnodes.index()
    indexnode['entries'] = [('single', termtext, node_id, 'main', index_key)]
    indexnode.source, indexnode.line = term.source, term.line
    term.append(indexnode)

    return term


class Glossary(SphinxDirective):
    """
    Directive to create a glossary with cross-reference targets for :term:
    roles.
    """

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec: OptionSpec = {
        'classifier': directives.unchanged,
        'sorted': directives.flag,
    }

    def run(self) -> List[Node]:

        # This directive implements a custom format of the reST definition list
        # that allows multiple lines of terms before the definition.  This is
        # easy to parse since we know that the contents of the glossary *must
        # be* a definition list.

        # first, collect single entries
        entries: List[Tuple[List[Tuple[str, str, int]], StringList]] = []
        in_definition = True
        in_comment = False
        was_empty = True
        messages: List[Node] = []
        for line, (source, lineno) in zip(self.content, self.content.items):
            # empty line -> add to last definition
            if not line:
                if in_definition and entries:
                    entries[-1][1].append('', source, lineno)
                was_empty = True
                continue
            # unindented line -> a term
            if line and not line[0].isspace():
                # enable comments
                if line.startswith('.. '):
                    in_comment = True
                    continue
                else:
                    in_comment = False

                # first term of definition
                if in_definition:
                    if not was_empty:
                        messages.append(self.state.reporter.warning(
                            _('glossary term must be preceded by empty line'),
                            source=source, line=lineno))
                    entries.append(([(line, source, lineno)], StringList()))
                    in_definition = False
                # second term and following
                else:
                    if was_empty:
                        messages.append(self.state.reporter.warning(
                            _('glossary terms must not be separated by empty lines'),
                            source=source, line=lineno))
                    if entries:
                        entries[-1][0].append((line, source, lineno))
                    else:
                        messages.append(self.state.reporter.warning(
                            _('glossary seems to be misformatted, check indentation'),
                            source=source, line=lineno))
            elif in_comment:
                pass
            else:
                if not in_definition:
                    # first line of definition, determines indentation
                    in_definition = True
                    indent_len = len(line) - len(line.lstrip())
                if entries:
                    entries[-1][1].append(line[indent_len:], source, lineno)
                else:
                    messages.append(self.state.reporter.warning(
                        _('glossary seems to be misformatted, check indentation'),
                        source=source, line=lineno))
            was_empty = False

        # now, parse all the entries into a big definition list
        return messages + self.make_glossary(entries)

    def _make_glossary_term(self, textnodes, index_key, source, lineno, node_id, document):
        return make_glossary_term(self.env, textnodes, index_key, source, lineno,
                                  node_id=node_id, document=document)

    def make_glossary(self, entries):
        node = addnodes.glossary()
        node.document = self.state.document
        node['sorted'] = ('sorted' in self.options)
        classifier = self.options.get('classifier')

        items: List[nodes.definition_list_item] = []
        for terms, definition in entries:
            termnodes: List[Node] = []
            system_messages: List[Node] = []
            for line, source, lineno in terms:
                parts = split_term_classifiers(line)
                # parse the term with inline markup
                # classifiers (parts[1:]) will not be shown on doctree
                textnodes, sysmsg = self.state.inline_text(parts[0], lineno)

                # use first classifier as a index key
                if classifier and not parts[1]:
                    parts[1] = classifier
                term = self._make_glossary_term(textnodes, parts[1], source, lineno,
                                               node_id=None, document=self.state.document)
                term.rawsource = line
                system_messages.extend(sysmsg)
                termnodes.append(term)

            termnodes.extend(system_messages)

            defnode = nodes.definition()
            if definition:
                self.state.nested_parse(definition, definition.items[0][1],
                                        defnode)
            termnodes.append(defnode)
            items.append(nodes.definition_list_item('', *termnodes))

        dlist = nodes.definition_list('', *items)
        dlist['classes'].append('glossary')
        node += dlist
        return [node]
