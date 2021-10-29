#!/usr/bin/python
import unittest
from docutils.parsers.rst.states import Inliner
from src import XRefIndex

#-------------------------------------------------------------------

inliner = Inliner()

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

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
