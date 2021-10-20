#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 

testcase01i = {
'doc1': [ ('single','sphinx','id-111','','clf'), ],
'doc2': [ ('single','sphinx','id-121','',None), ],
}

testcase01o = [
('clf',
  [('sphinx',
    [[('', 'doc1.html#id-111'),
      ('', 'doc2.html#id-121')],
     [],
     'clf'])])
]

testcase02i = {
'doc1': [ ('single','sphinx','id-211','',None), ],
'doc2': [ ('single','sphinx','id-221','','clr'), ],
}

testcase02o = [
('clr',
  [('sphinx',
    [[('', 'doc1.html#id-211'), ('', 'doc2.html#id-221')], [], None])])]

#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_classifier_catalog(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase01o)

    def test02_classifier_catalog(self):
        self.maxDiff = None
        env = util.env(testcase02i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase02o)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
