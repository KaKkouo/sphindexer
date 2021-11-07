#!/usr/bin/python
import unittest
from unittest.mock import Mock, MagicMock
from docutils import nodes
from src import patch as pch

#-------------------------------------------------------------------


#-------------------------------------------------------------------


class testTerm(unittest.TestCase):
    def test01_basic(self):
        text = "sphinx"
        term = pch.term(text, text)
        self.assertEqual(term[0], "sphinx") 

    def test02_basic(self):
        text = nodes.Text("sphinx")
        term = pch.term(text, '', text)
        self.assertEqual(term[0], "sphinx") 


#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
