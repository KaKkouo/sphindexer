#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 


testcase03i = {
'doc1': [ ('single','func1() (bbbb module)','id-311','',None),],
'doc2': [ ('single','func1() (aaaa module)','id-321','',None),],
}

testcase03o = [
('F',
  [('func1()',
    [[],
     [('(aaaa module)', [('', 'doc2.html#id-321')]),
      ('(bbbb module)', [('', 'doc1.html#id-311')])],
     None])])
]

testcase04i = {
'doc1': [ ('single','func1() (doc1 module)','id-411','',None),],
'doc2': [ ('single','func2() (doc2 module)','id-421','',None),],
'doc3': [ ('single','func1() (doc3 module)','id-431','',None),],
'doc4': [ ('single','func2() (odc4 module)','id-441','',None),],
}

testcase04o = [
('F',
  [('func1()',
    [[],
     [('(doc1 module)', [('', 'doc1.html#id-411')]),
      ('(doc3 module)', [('', 'doc3.html#id-431')])],
     None]),
   ('func2()',
    [[],
     [('(doc2 module)', [('', 'doc2.html#id-421')]),
      ('(odc4 module)', [('', 'doc4.html#id-441')])],
     None])])
]

testcase05i = {
'doc1': [ ('single','func1() (bbbb module)','id-511','',None),],
'doc2': [ ('single','func2() (bbbb module)','id-521','',None),],
'doc3': [ ('single','func1() (aaaa module)','id-531','',None),],
'doc4': [ ('single','func2() (aaaa module)','id-541','',None),],
}

testcase05o = [
('F',
  [('func1()',
    [[],
     [('(aaaa module)', [('', 'doc3.html#id-531')]),
      ('(bbbb module)', [('', 'doc1.html#id-511')])],
     None]),
   ('func2()',
    [[],
     [('(aaaa module)', [('', 'doc4.html#id-541')]),
      ('(bbbb module)', [('', 'doc2.html#id-521')])],
     None])])
]

testcase06i = {
'doc1': [ ('single','func1()','id-611','',None),],
'doc2': [ ('single','func1() (doc2 module)','id-621','',None),],
'doc3': [ ('single','func1() (doc3 module)','id-631','',None),],
'doc4': [ ('single','func1()','id-641','',None),],
}

testcase06o = [
('F',
  [('func1()',
    [[('', 'doc1.html#id-611'), ('', 'doc4.html#id-641')],
     [('(doc2 module)', [('', 'doc2.html#id-621')]),
      ('(doc3 module)', [('', 'doc3.html#id-631')])],
     None])])
]

testcase07i = {
'doc1': [ ('single','func1()','id-711','',None),],
'doc2': [ ('single','func1() (doc2 module)','id-721','',None),],
'doc3': [ ('single','func1() (doc3 module)','id-731','',None),],
'doc4': [ ('single','func1()','id-741','main',None),],
}

testcase07o = [
('F',
  [('func1()',
    [[('main', 'doc4.html#id-741'), ('', 'doc1.html#id-711')],
     [('(doc2 module)', [('', 'doc2.html#id-721')]),
      ('(doc3 module)', [('', 'doc3.html#id-731')])],
     None])])
]

testcase08i = {
'doc1': [ ('single','func1() (doc1 module); sphinx','id-811','',None),],
'doc2': [ ('single','func2() (doc2 module); sphinx','id-821','',None),],
'doc3': [ ('single','func1() (doc3 module); python','id-831','',None),],
'doc4': [ ('single','func2() (odc4 module); python','id-841','',None),],
}

testcase08o = [
('F',
  [('func1()',
    [[],
     [('(doc1 module), sphinx', [('', 'doc1.html#id-811')]),
      ('(doc3 module), python', [('', 'doc3.html#id-831')])],
     None]),
  ('func2()',
    [[],
     [('(doc2 module), sphinx', [('', 'doc2.html#id-821')]),
      ('(odc4 module), python', [('', 'doc4.html#id-841')])],
     None])])
]

#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_function_catalog(self):
        testcase = {
            'doc1': [ ('single','func1() (aaa module)','id-111','',None), ]
        }
        env = util.env(testcase)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(len(gidx), 1)
        self.assertEqual(gidx[0][0], 'F')
        self.assertEqual(
            gidx[0][1], 
            [('func1() (aaa module)', [[('', 'doc1.html#id-111')], [], None])])

    def test02_function_catalog(self):
        testcase = {
            'doc1': [ ('single','func1() (doc1 module)','id-211','',None),],
            'doc2': [ ('single','func1() (doc2 module)','id-221','',None),],
        }
        env = util.env(testcase)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(len(gidx), 1)
        self.assertEqual(gidx[0][0], 'F')
        self.assertEqual(
            gidx[0][1], 
            [('func1()', [[],
                          [('(doc1 module)', [('', 'doc1.html#id-211')]),
                           ('(doc2 module)', [('', 'doc2.html#id-221')])],
                          None])])

    def test03_function_catalog(self):
        self.maxDiff = None
        env = util.env(testcase03i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase03o)

    def test04_function_catalog(self):
        self.maxDiff = None
        env = util.env(testcase04i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase04o)

    def test05_function_catalog(self):
        self.maxDiff = None
        env = util.env(testcase05i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase05o)

    def test06_function_catalog(self):
        self.maxDiff = None
        env = util.env(testcase06i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase06o)

    def test07_function_catalog(self):
        self.maxDiff = None
        env = util.env(testcase07i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase07o)

    def test08_function_catalog(self):
        self.maxDiff = None
        env = util.env(testcase08i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(gidx, testcase08o)

    def test09_function_catalog(self):
        testcase = {
            'doc1': [ ('single','func1() (doc1 module)','id-211','',None),],
            'doc2': [ ('single','func1() (doc2 module)','id-221','',None),],
        }
        env = util.env(testcase)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld, False)
        self.assertEqual(len(gidx), 1)
        self.assertEqual(gidx[0][0], 'F')
        self.assertEqual(
            gidx[0][1], 
            [('func1() (doc1 module)', [[('', 'doc1.html#id-211')], [], None]),
             ('func1() (doc2 module)', [[('', 'doc2.html#id-221')], [], None])])

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
