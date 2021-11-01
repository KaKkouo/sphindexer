#!/usr/bin/python
import unittest
from src import IndexRack
from . import util 

testcase01i = { 
    'doc1': [('single', 'docutils', 'id-111', '', None),
             ('single', 'Python', 'id-112', '', None), ], 
    'doc2': [('single', 'pip; install', 'id-121', '', None),
             ('single', 'pip; upgrade', 'id-122', '', None), ],
    'doc3': [('single', 'Sphinx', 'id-131', '', None),
             ('single', 'Ель', 'id-132', '', None), ], 
    'doc4': [('single', 'ёлка', 'id-141', '', None),
             ('single', "‏עברית‎", 'id-142', '', None), ], 
    'doc5': [('single', '9-symbol', 'id-151', '', None),
             ('single', '&-symbol', 'id-152', '', None), ], 
    'doc6': [('single', '£100', 'id-161', '', None), ], 
}

testcase01o0 = ('Symbols', [('&-symbol', [[('', 'doc5.html#id-152')], [], None]),
                            ('9-symbol', [[('', 'doc5.html#id-151')], [], None]),
                            ('£100', [[('', 'doc6.html#id-161')], [], None])])
testcase01o1 = ('D', [('docutils', [[('', 'doc1.html#id-111')], [], None])])
testcase01o2 = ('P', [('pip', [[],
                      [('install', [('', 'doc2.html#id-121')]),
                       ('upgrade', [('', 'doc2.html#id-122')])],
                      None]),
                      ('Python', [[('', 'doc1.html#id-112')], [], None])])
testcase01o3 = ('S', [('Sphinx', [[('', 'doc3.html#id-131')], [], None])])
testcase01o4 = ('Е', [('ёлка', [[('', 'doc4.html#id-141')], [], None]),
                      ('Ель', [[('', 'doc3.html#id-132')], [], None])])
testcase01o5 = ('ע', [('‏עברית‎', [[('', 'doc4.html#id-142')], [], None])])


#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_special_letter(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(len(gidx), 6)
        self.assertEqual(gidx[0], testcase01o0)
        self.assertEqual(gidx[1], testcase01o1)
        self.assertEqual(gidx[2], testcase01o2)
        self.assertEqual(gidx[3], testcase01o3)
        self.assertEqual(gidx[4], testcase01o4)
        self.assertEqual(gidx[5], testcase01o5)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
