#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 

testcase01i = {
'doc1': [ ('single','sphinx; reST','id-711','',None), ],
'doc2': [ ('single','python; ruby','id-721','',None), ],
'doc3': [ ('single','sphinx','id-731','',None), ],
'doc4': [ ('single','python','id-741','',None), ],
'doc5': [ ('single','sphinx','id-751','',None), ],
'doc6': [ ('single','python','id-761','',None), ],
}

testcase01o = [
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

testcase02i = {
'doc1': [ ('single','sphinx; reST','id-811','',None), ],
'doc2': [ ('single','python; ruby','id-821','',None), ],
'doc3': [ ('single','sphinx','id-831','',None), ],
'doc4': [ ('single','python','id-841','',None), ],
'doc5': [ ('single','sphinx','id-851','main',None), ],
'doc6': [ ('single','python','id-861','main',None), ],
}

testcase02o = [
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

testcase03i = {
'doc1': [ ('single','sphinx; reST','id-911','',None), ],
'doc2': [ ('single','python; ruby','id-921','',None), ],
'doc5': [ ('single','sphinx','id-931','',None), ],
'doc6': [ ('single','python','id-941','',None), ],
'doc3': [ ('single','sphinx','id-951','main',None), ],
'doc4': [ ('single','python','id-961','main',None), ],
}

testcase03o = [
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
    def test01_single_term_with_sub(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase01o)

    def test02_single_term_with_sub(self):
        self.maxDiff = None
        env = util.env(testcase02i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase02o)

    def test03_single_term_with_sub(self):
        self.maxDiff = None
        env = util.env(testcase03i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase03o)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
