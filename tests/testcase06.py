#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 

testcase01i = {
'doc1': [ ('pair','sphinx; reST','id-111','',None), ],
}

testcase01o = [
('R',
  [('reST',
    [[],
     [('sphinx', [('', 'doc1.html#id-111')])],
     None])]),
 ('S',
  [('sphinx',
    [[],
     [('reST', [('', 'doc1.html#id-111')])],
     None])])
]

testcase02i = {
'doc1': [ ('pair','sphinx; reST','id-211','',None), ],
'doc2': [ ('pair','python; ruby','id-221','',None), ],
'doc3': [ ('pair','ruby; php',   'id-231','',None), ],
'doc4': [ ('pair','php; python', 'id-241','',None), ],
}

testcase02o = [
('P',
 [('php',
    [[],
     [('python', [('', 'doc4.html#id-241')]),
      ('ruby', [('', 'doc3.html#id-231')])],
     None]),
   ('python',
    [[],
     [('php', [('', 'doc4.html#id-241')]),
      ('ruby', [('', 'doc2.html#id-221')])],
     None])]),
('R',
  [('reST',
    [[],
     [('sphinx', [('', 'doc1.html#id-211')])],
     None]),
   ('ruby',
    [[],
     [('php', [('', 'doc3.html#id-231')]),
      ('python', [('', 'doc2.html#id-221')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('reST', [('', 'doc1.html#id-211')])],
     None])])
]

testcase03i = {
'doc1': [ ('pair','sphinx; python','id-311','',None), ],
'doc2': [ ('single','sphinx','id-321','',None), ],
'doc3': [ ('single','python','id-331','',None), ],
}

testcase03o = [
('P',
  [('python',
    [[('', 'doc3.html#id-331')],
     [('sphinx', [('', 'doc1.html#id-311')])],
     None])]),
('S',
  [('sphinx',
    [[('', 'doc2.html#id-321')],
     [('python', [('', 'doc1.html#id-311')])],
     None])])
]

testcase04i = {
'doc1': [ ('pair','sphinx; python','id-411','',None), ],
'doc2': [ ('single','sphinx; python','id-421','',None), ],
'doc3': [ ('single','python; sphinx','id-431','',None), ],
}

testcase04o = [
('P',
  [('python',
    [[],
     [('sphinx',
       [('', 'doc1.html#id-411'),
        ('', 'doc3.html#id-431')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('python',
       [('', 'doc1.html#id-411'),
        ('', 'doc2.html#id-421')])],
     None])])
]

testcase05i = {
'doc1': [ ('pair','sphinx; python','id-511','',None), ],
'doc2': [ ('single','sphinx; python','id-521','main',None), ],
'doc3': [ ('single','python; sphinx','id-531','main',None), ],
}

testcase05o = [
('P',
  [('python',
    [[],
     [('sphinx',
       [('main', 'doc3.html#id-531'), ('', 'doc1.html#id-511')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('python',
       [('main', 'doc2.html#id-521'), ('', 'doc1.html#id-511')])],
     None])])
]

testcase06i = {
'doc3': [ ('pair','sphinx; python','id-611','',None), ],
'doc1': [ ('single','sphinx; python','id-621','',None), ],
'doc2': [ ('single','python; sphinx','id-631','',None), ],
}

testcase06o = [
('P',
  [('python',
    [[],
     [('sphinx',
       [('', 'doc2.html#id-631'), ('', 'doc3.html#id-611')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('python',
       [('', 'doc1.html#id-621'), ('', 'doc3.html#id-611')])],
     None])])
]

testcase07i = {
'doc3': [ ('pair','sphinx; python','id-711','main',None), ],
'doc1': [ ('single','sphinx; python','id-721','',None), ],
'doc2': [ ('single','python; sphinx','id-731','',None), ],
}

testcase07o = [
('P',
  [('python',
    [[],
     [('sphinx',
       [('main', 'doc3.html#id-711'), ('', 'doc2.html#id-731')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('python',
       [('main', 'doc3.html#id-711'), ('', 'doc1.html#id-721')])],
     None])])
]

#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_pair(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase01o)

    def test02_pair(self):
        self.maxDiff = None
        env = util.env(testcase02i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase02o)

    def test03_pair_and_single(self):
        self.maxDiff = None
        env = util.env(testcase03i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase03o)

    def test04_pair_and_single(self):
        self.maxDiff = None
        env = util.env(testcase04i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase04o)

    def test05_pair_and_single(self):
        self.maxDiff = None
        env = util.env(testcase05i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase05o)

    def test06_pair_and_single(self):
        self.maxDiff = None
        env = util.env(testcase06i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase06o)

    def test07_pair_and_single(self):
        self.maxDiff = None
        env = util.env(testcase07i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase07o)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
