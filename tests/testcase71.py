#!/usr/bin/python
import unittest
from docutils.parsers.rst.states import Inliner
from sphinx.application import Sphinx
from sphinx.errors import SphinxError

#-------------------------------------------------------------------

inliner = Inliner()

workdir = 'tests'
distdir = workdir + '/tmp'

#-------------------------------------------------------------------

class testBuilder(unittest.TestCase):
    def test01_AttributeError(self):
        application = Sphinx(workdir, workdir, distdir, distdir, "idxr")
        bld = application.builder
        with self.assertRaises(AttributeError):
            bld.write_genindex()

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
