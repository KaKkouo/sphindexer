#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 

testcase01i = {
'doc1': [ ('single','sphinx','id-111','',None), ],
'doc2': [ ('single','python','id-121','',None), ],
}

testcase01o = [
('P', [('python', [[('', 'doc2.html#id-121')], [], None])]),
('S', [('sphinx', [[('', 'doc1.html#id-111')], [], None])])
]

testcase02i = {
'doc1': [ ('single','sphinx','id-211','',None), ],
'doc2': [ ('single','sphinx','id-221','',None), ],
}

testcase02o = [
('S',
  [('sphinx',
    [[('', 'doc1.html#id-211'), ('', 'doc2.html#id-221')], [], None])])
]

testcase03i = {
'doc1': [ ('single','sphinx','id-311','main',None), ],
'doc2': [ ('single','sphinx','id-321','',None), ],
}

testcase03o = [
('S',
  [('sphinx',
    [[('main', 'doc1.html#id-311'), ('', 'doc2.html#id-321')], [], None])])
]

testcase04i = {
'doc1': [ ('single','sphinx','id-411','',None), ],
'doc2': [ ('single','sphinx','id-421','main',None), ],
}

testcase04o = [
('S',
  [('sphinx',
    [[('main', 'doc2.html#id-421'), ('', 'doc1.html#id-411')], [], None])])
]

testcase05i = {
'doc1': [ ('single','sphinx','id-511','main',None), ],
'doc2': [ ('single','sphinx','id-521','main',None), ],
}

testcase05o = [
('S',
  [('sphinx',
    [[('main', 'doc1.html#id-511'), ('main', 'doc2.html#id-521')], [], None])])
]

testcase06i = {
'doc1': [ ('single','sphinx','id-611','',None), ],
'doc2': [ ('single','sphinx','id-621','',None), ],
'doc3': [ ('single','python','id-631','',None), ],
'doc4': [ ('single','python','id-641','',None), ],
}

testcase06o = [
('P',
  [('python',
    [[('', 'doc3.html#id-631'), ('', 'doc4.html#id-641')], [], None])]),
 ('S',
  [('sphinx',
    [[('', 'doc1.html#id-611'), ('', 'doc2.html#id-621')], [], None])])
]

testcase07i = {
'doc1': [ ('single','sphinx','id-711','',None), ],
'doc2': [ ('single','sphinx','id-721','main',None), ],
'doc3': [ ('single','python','id-731','',None), ],
'doc4': [ ('single','python','id-741','main',None), ],
}

testcase07o = [
('P',
  [('python',
    [[('main', 'doc4.html#id-741'), ('', 'doc3.html#id-731')], [], None])]),
 ('S',
  [('sphinx',
    [[('main', 'doc2.html#id-721'), ('', 'doc1.html#id-711')], [], None])])
]

#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_single_one_term(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase01o)

    def test02_single_one_term(self):
        self.maxDiff = None
        env = util.env(testcase02i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase02o)

    def test03_single_one_term(self):
        self.maxDiff = None
        env = util.env(testcase03i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase03o)

    def test04_single_one_term(self):
        self.maxDiff = None
        env = util.env(testcase04i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase04o)

    def test05_single_one_term(self):
        self.maxDiff = None
        env = util.env(testcase05i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase05o)

    def test06_single_one_term(self):
        self.maxDiff = None
        env = util.env(testcase06i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase06o)

    def test07_single_one_term(self):
        self.maxDiff = None
        env = util.env(testcase07i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase07o)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
