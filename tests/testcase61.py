#!/usr/bin/python
import unittest
from unittest.mock import Mock, MagicMock
from docutils import nodes
from docutils.parsers.rst.states import Inliner
from sphinx.testing.util import assert_node
from src import XRefIndex

#-------------------------------------------------------------------

inliner = Inliner()

def get_source_info(lineno):
    return ('doc1', lineno)

#-------------------------------------------------------------------

class testXRefIndex(unittest.TestCase):
    def test01_textclass(self):
        xref = XRefIndex()
        text = xref.textclass('sphinx', 'sphinx')
        self.assertEqual('sphinx', text)

    def test02_AttributeError(self):
        xref = XRefIndex()
        with self.assertRaises(AttributeError):
            rslt = xref('index', 'sphinx', 'sphinx', 1, inliner, {}, [])

    def test03_TypeError(self):
        text = 'sphinx<python>'
        xref = XRefIndex()
        with self.assertRaises(TypeError):
            rslt, msg = xref('index', text, text, 0, Mock())

    def test04_TypeError(self):
        text = 'sphinx'
        xref = XRefIndex()
        with self.assertRaises(TypeError):
            rslt, msg = xref('index', text, text, 1, Mock())

    def test05_TypeError(self):
        text = '!sphinx'
        xref = XRefIndex()
        with self.assertRaises(TypeError):
            rslt, msg = xref('index', text, text, 1, Mock())

    def test06_ValueError(self):
        text = 'sphinx<python>'
        mock = MagicMock(return_value=(1, "msg"))
        xref = XRefIndex()
        with self.assertRaises(ValueError):
            rslt, msg = xref('index', text, text, 1, mock)

    def test07_AssertionError(self):
        text = 'sphinx<python>'
        mock1 = MagicMock(return_value=(1, "msg"))
        mock2 = MagicMock(return_value=(1, "msg"))
        inliner.document = mock1
        inliner.reporter = mock2
        xref = XRefIndex()
        xref.get_source_info = get_source_info
        nodes, msg = xref('index', text, text, len(text), inliner)
        node = nodes[0]
        with self.assertRaises(AssertionError):
            self.assertEqual(node, "")

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
