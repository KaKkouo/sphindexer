#!/usr/bin/python
import unittest
from docutils.parsers.rst.states import Inliner
from sphinx.application import Sphinx
from sphinx.errors import SphinxError

from src.glossary import BaseGlossary

#-------------------------------------------------------------------

inliner = Inliner()

workdir = 'tests'
distdir = workdir + '/out'

#-------------------------------------------------------------------

class testBuilder(unittest.TestCase):
    def test01_build(self):
        application = Sphinx(workdir, workdir, distdir, distdir, "idxr")
        application.add_directive('glossary', BaseGlossary, True)
        bld = application.builder

        with self.assertRaises(AttributeError):
            bld.write_genindex()

        application.build(False, ['tests/index.rst'])
        bld.config.html_split_index = True
        bld.write_genindex()

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
