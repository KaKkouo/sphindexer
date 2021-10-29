#!/usr/bin/python
import unittest
from docutils.parsers.rst.states import Inliner
from sphinx.application import Sphinx
from sphinx.errors import SphinxError
from src import _StandaloneHTMLBuilder as BaseBuilder, setup

#-------------------------------------------------------------------

inliner = Inliner()

workdir = 'tests'
distdir = workdir + '/tmp'

#-------------------------------------------------------------------

class testBaseBuilder(unittest.TestCase):
    def test01_setup(self):
        with self.assertRaises(SphinxError):
            application = Sphinx(workdir, workdir, distdir, distdir, BaseBuilder)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
