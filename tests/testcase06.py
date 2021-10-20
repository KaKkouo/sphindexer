#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 

testcase01i = {
'doc1': [ ('triple','bash; perl; tcsh','id-111','',None), ],
}

testcase01o = [
('B',
  [('bash',
    [[],
     [('perl tcsh', [('', 'doc1.html#id-111')])],
     None])]),
('P',
  [('perl',
    [[],
     [('tcsh, bash', [('', 'doc1.html#id-111')])],
     None])]),
('T',
  [('tcsh',
    [[],
     [('bash perl', [('', 'doc1.html#id-111')])],
     None])])
]

testcase02i = {
'doc1': [ ('triple','bash; perl; tcsh','id-211','',None), ],
'doc2': [ ('single','bash; perl','id-221','',None), ],
'doc3': [ ('single','perl; tcsh','id-231','',None), ],
'doc4': [ ('single','tcsh; bash','id-241','',None), ],
}

testcase02o = [
('B',
  [('bash',
    [[],
     [('perl', [('', 'doc2.html#id-221')]),
      ('perl tcsh', [('', 'doc1.html#id-211')])],
     None])]),
 ('P',
  [('perl',
    [[],
     [('tcsh', [('', 'doc3.html#id-231')]),
      ('tcsh, bash', [('', 'doc1.html#id-211')])],
     None])]),
 ('T',
  [('tcsh',
    [[],
     [('bash', [('', 'doc4.html#id-241')]),
      ('bash perl', [('', 'doc1.html#id-211')])],
     None])])
]

testcase03i = {
'doc1': [ ('triple','bash; perl; tcsh','id-311','',None), ],
'doc2': [ ('single','bash; perl tcsh','id-321','',None), ],
'doc3': [ ('single','perl; tcsh, bash','id-331','',None), ],
'doc4': [ ('single','tcsh; bash perl','id-341','',None), ],
}

testcase03o = [
('B',
  [('bash',
    [[],
     [('perl tcsh',
       [('', 'doc1.html#id-311'), ('', 'doc2.html#id-321')])],
     None])]),
('P',
  [('perl',
    [[],
     [('tcsh, bash',
       [('', 'doc1.html#id-311'), ('', 'doc3.html#id-331')])],
     None])]),
('T',
  [('tcsh',
    [[],
     [('bash perl',
       [('', 'doc1.html#id-311'), ('', 'doc4.html#id-341')])],
     None])])
]

testcase04i = {
'doc1': [ ('triple','bash; perl; tcsh','id-411','',None), ],
'doc2': [ ('single','bash; perl tcsh','id-421','main',None), ],
'doc3': [ ('single','perl; tcsh, bash','id-431','main',None), ],
'doc4': [ ('single','tcsh; bash perl','id-441','main',None), ],
}

testcase04o = [
('B',
  [('bash',
    [[],
     [('perl tcsh',
       [('main', 'doc2.html#id-421'), ('', 'doc1.html#id-411')])],
     None])]),
('P',
  [('perl',
    [[],
     [('tcsh, bash',
       [('main', 'doc3.html#id-431'), ('', 'doc1.html#id-411')])],
     None])]),
 ('T',
  [('tcsh',
    [[],
     [('bash perl',
       [('main', 'doc4.html#id-441'), ('', 'doc1.html#id-411')])],
     None])])
]

testcase05i = {
'doc1': [ ('single','bash; perl tcsh','id-511','',None), ],
'doc2': [ ('single','perl; tcsh, bash','id-521','',None), ],
'doc3': [ ('single','tcsh; bash perl','id-531','',None), ],
'doc4': [ ('triple','bash; perl; tcsh','id-541','main',None), ],
}

testcase05o = [
('B',
  [('bash',
    [[],
     [('perl tcsh',
       [('main', 'doc4.html#id-541'), ('', 'doc1.html#id-511')])],
     None])]),
('P',
  [('perl',
    [[],
     [('tcsh, bash',
       [('main', 'doc4.html#id-541'), ('', 'doc2.html#id-521')])],
     None])]),
('T',
  [('tcsh',
    [[],
     [('bash perl',
       [('main', 'doc4.html#id-541'), ('', 'doc3.html#id-531')])],
     None])])]

#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_triple(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase01o)

    def test02_triple_with_single(self):
        self.maxDiff = None
        env = util.env(testcase02i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase02o)

    def test03_triple_with_single(self):
        self.maxDiff = None
        env = util.env(testcase03i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase03o)

    def test04_triple_with_single(self):
        self.maxDiff = None
        env = util.env(testcase04i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase04o)

    def test05_triple_with_single(self):
        self.maxDiff = None
        env = util.env(testcase05i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase05o)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
