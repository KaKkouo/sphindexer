#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 

testcase01i = {
'doc1': [
    ('single','func1() (aaa module)','id-111','',None), ]
}

testcase01o = [
('F',
  [('func1() (aaa module)', [[('', 'doc1.html#id-111')], [], None])])
]


testcase02i = {
'doc1': [
    ('single','func1() (doc1 module)','id-211','',None),],
'doc2': [
    ('single','func1() (doc2 module)','id-221','',None),],
}

testcase02o = [
('F',
  [('func1()',
    [[],
     [('(doc1 module)', [('', 'doc1.html#id-211')]),
      ('(doc2 module)', [('', 'doc2.html#id-221')])],
     None])])
]


testcase03i = {
'doc1': [
    ('single','func1() (aaa module)','id-311','',None),
    ('single','func1() (bbb module)','id-312','',None),
    ('single','func1() (ccc module)','id-313','',None),]
}

testcase03o = [
('F',
  [('func1()',
    [[],
     [('(aaa module)', [('', 'doc1.html#id-311')]),
      ('(bbb module)', [('', 'doc1.html#id-312')]),
      ('(ccc module)', [('', 'doc1.html#id-313')])
     ],
     None])])
]


testcase04i = {
'doc1': [
    ('single','func1() (aaa module)','id-411','',None),
    ('single','func1() (bbb module)','id-412','',None),
    ('single','func1() (ccc module)','id-413','main',None), ]
}

testcase04o = [
('F',
  [('func1()',
    [[],
     [('(aaa module)', [('', 'doc1.html#id-411')]),
      ('(bbb module)', [('', 'doc1.html#id-412')]),
      ('(ccc module)', [('main', 'doc1.html#id-413')]), ],
     None])])
]

#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_homonymous_function(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase01o)

    def test02_homonymous_function(self):
        self.maxDiff = None
        env = util.env(testcase02i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase02o)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
