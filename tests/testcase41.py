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

testcase03i = {
'doc1': [ ('single','python','id-311','',None), ],
'doc2': [ ('single','sphinx; directive','id-321','',None), ],
'doc3': [ ('see','sphinx; python','id-331','',None), ],
'doc4': [ ('single','sphinx; role','id-341','',None), ],
}

testcase03o = [
('P', [('python', [[('', 'doc1.html#id-311')], [], None])]),
('S',
  [('sphinx',
    [[],
     [('see python', []),
      ('directive', [('', 'doc2.html#id-321')]),
      ('role', [('', 'doc4.html#id-341')])],
     None])])
]

testcase04i = {
'doc1': [ ('single','python','id-411','',None), ],
'doc2': [ ('single','sphinx; directive','id-421','',None), ],
'doc3': [ ('seealso','sphinx; python','id-431','',None), ],
'doc4': [ ('single','sphinx; role','id-441','',None), ],
}

testcase04o = [
('P', [('python', [[('', 'doc1.html#id-411')], [], None])]),
('S',
  [('sphinx',
    [[],
     [('see also python', []),
      ('directive', [('', 'doc2.html#id-421')]),
      ('role', [('', 'doc4.html#id-441')])],
     None])])
]

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

    def test03_see_seealso(self):
        self.maxDiff = None
        env = util.env(testcase03i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase03o)

    def test04_see_seealso(self):
        self.maxDiff = None
        env = util.env(testcase04i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase04o)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
