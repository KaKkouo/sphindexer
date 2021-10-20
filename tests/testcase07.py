#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 

testcase01i = {
'doc1': [ ('single','python','id-111','',None), ],
'doc2': [ ('see','sphinx; python','id-121','',None), ],
}

testcase01o = [
('P', [('python', [[('', 'doc1.html#id-111')], [], None])]),
('S', [('sphinx', [[], [('see python', [])], None])])
]

testcase02i = {
'doc1': [ ('single','python','id-211','',None), ],
'doc2': [ ('seealso','sphinx; python','id-221','',None), ],
}

testcase02o = [
('P', [('python', [[('', 'doc1.html#id-211')], [], None])]),
('S', [('sphinx', [[], [('see also python', [])], None])])]

#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_see_seealso(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase01o)

    def test02_see_seealso(self):
        self.maxDiff = None
        env = util.env(testcase02i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase02o)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
