#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 

testcase01i = {
'doc1': [ ('single','sphinx; bash','id-111','',None), ],
'doc2': [ ('single','python; php','id-121','',None), ],
}

testcase01o = [
('P',
  [('python',
    [[],
     [('php', [('', 'doc2.html#id-121')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('bash', [('', 'doc1.html#id-111')])],
     None])])
]

testcase02i = {
'doc1': [ ('single','sphinx; tcsh','id-211','',None), ],
'doc2': [ ('single','python; ruby','id-221','',None), ],
'doc3': [ ('single','sphinx; bash','id-231','',None), ],
'doc4': [ ('single','python; perl','id-241','',None), ],
}

testcase02o = [
('P',
  [('python',
    [[],
     [('perl', [('', 'doc4.html#id-241')]),
      ('ruby', [('', 'doc2.html#id-221')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('bash', [('', 'doc3.html#id-231')]),
      ('tcsh', [('', 'doc1.html#id-211')])],
     None])])
]

testcase03i = {
'doc1': [ ('single','sphinx; sphinx','id-311','',None), ],
'doc2': [ ('single','python; python','id-321','',None), ],
'doc3': [ ('single','sphinx; sphinx','id-331','',None), ],
'doc4': [ ('single','python; python','id-341','',None), ],
}

testcase03o = [
('P',
  [('python',
    [[],
     [('python',
       [('', 'doc2.html#id-321'), ('', 'doc4.html#id-341')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('sphinx',
       [('', 'doc1.html#id-311'), ('', 'doc3.html#id-331')])],
     None])])
]

testcase04i = {
'doc1': [ ('single','sphinx; sphinx','id-411','',None), ],
'doc2': [ ('single','python; python','id-421','',None), ],
'doc3': [ ('single','sphinx; sphinx','id-431','main',None), ],
'doc4': [ ('single','python; python','id-441','main',None), ],
}

testcase04o = [
('P',
  [('python',
    [[],
     [('python',
       [('main', 'doc4.html#id-441'), ('', 'doc2.html#id-421')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('sphinx',
       [('main', 'doc3.html#id-431'), ('', 'doc1.html#id-411')])],
     None])])
]

testcase05i = {
'doc1': [ ('single','sphinx; sphinx','id-511','',None), ],
'doc2': [ ('single','python; python','id-521','',None), ],
'doc5': [ ('single','sphinx; sphinx','id-531','main',None), ],
'doc6': [ ('single','python; python','id-541','main',None), ],
'doc3': [ ('single','sphinx; sphinx','id-551','main',None), ],
'doc4': [ ('single','python; python','id-561','main',None), ],
}

testcase05o = [
('P',
  [('python',
    [[],
     [('python',
       [('main', 'doc4.html#id-561'),
        ('main', 'doc6.html#id-541'),
        ('', 'doc2.html#id-521')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('sphinx',
       [('main', 'doc3.html#id-551'),
        ('main', 'doc5.html#id-531'),
        ('', 'doc1.html#id-511')])],
     None])])
]

testcase06i = {
'doc3': [ ('single','sphinx; reST','id-611','',None), ],
'doc4': [ ('single','python; ruby','id-621','',None), ],
'doc1': [ ('single','sphinx; reST','id-631','',None), ],
'doc2': [ ('single','python; ruby','id-641','',None), ],
}

testcase06o = [
('P',
  [('python',
    [[],
     [('ruby',
       [('', 'doc2.html#id-641'), ('', 'doc4.html#id-621')])],
     None])]),
('S',
  [('sphinx',
    [[],
     [('reST',
       [('', 'doc1.html#id-631'), ('', 'doc3.html#id-611')])],
     None])])
]

testcase07i = {
'doc1': [ ('single','sphinx; reST','id-711','',None), ],
'doc2': [ ('single','python; ruby','id-721','',None), ],
'doc3': [ ('single','sphinx','id-731','',None), ],
'doc4': [ ('single','python','id-741','',None), ],
'doc5': [ ('single','sphinx','id-751','',None), ],
'doc6': [ ('single','python','id-761','',None), ],
}

testcase07o = [
('P',
  [('python',
    [[('', 'doc4.html#id-741'), ('', 'doc6.html#id-761')],
     [('ruby', [('', 'doc2.html#id-721')])],
     None])]),
('S',
  [('sphinx',
    [[('', 'doc3.html#id-731'), ('', 'doc5.html#id-751')],
     [('reST', [('', 'doc1.html#id-711')])],
     None])])
]

testcase08i = {
'doc1': [ ('single','sphinx; reST','id-811','',None), ],
'doc2': [ ('single','python; ruby','id-821','',None), ],
'doc3': [ ('single','sphinx','id-831','',None), ],
'doc4': [ ('single','python','id-841','',None), ],
'doc5': [ ('single','sphinx','id-851','main',None), ],
'doc6': [ ('single','python','id-861','main',None), ],
}

testcase08o = [
('P',
  [('python',
    [[('main', 'doc6.html#id-861'), ('', 'doc4.html#id-841')],
     [('ruby', [('', 'doc2.html#id-821')])],
     None])]),
('S',
  [('sphinx',
    [[('main', 'doc5.html#id-851'), ('', 'doc3.html#id-831')],
     [('reST', [('', 'doc1.html#id-811')])],
     None])])
]

testcase09i = {
'doc1': [ ('single','sphinx; reST','id-911','',None), ],
'doc2': [ ('single','python; ruby','id-921','',None), ],
'doc5': [ ('single','sphinx','id-931','',None), ],
'doc6': [ ('single','python','id-941','',None), ],
'doc3': [ ('single','sphinx','id-951','main',None), ],
'doc4': [ ('single','python','id-961','main',None), ],
}

testcase09o = [
('P',
  [('python',
    [[('main', 'doc4.html#id-961'), ('', 'doc6.html#id-941')],
     [('ruby', [('', 'doc2.html#id-921')])],
     None])]),
('S',
  [('sphinx',
    [[('main', 'doc3.html#id-951'), ('', 'doc5.html#id-931')],
     [('reST', [('', 'doc1.html#id-911')])],
     None])])
]

#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_single_subterm(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase01o)

    def test02_single_subterm(self):
        self.maxDiff = None
        env = util.env(testcase02i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase02o)

    def test03_single_subterm(self):
        self.maxDiff = None
        env = util.env(testcase03i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase03o)

    def test04_single_subterm(self):
        self.maxDiff = None
        env = util.env(testcase04i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase04o)

    def test05_single_subterm(self):
        self.maxDiff = None
        env = util.env(testcase05i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase05o)

    def test06_single_subterm(self):
        self.maxDiff = None
        env = util.env(testcase06i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase06o)

    def test07_single_term_with_sub(self):
        self.maxDiff = None
        env = util.env(testcase07i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase07o)

    def test08_single_term_with_sub(self):
        self.maxDiff = None
        env = util.env(testcase08i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase08o)

    def test09_single_term_with_sub(self):
        self.maxDiff = None
        env = util.env(testcase09i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase09o)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
