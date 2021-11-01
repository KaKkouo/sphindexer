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
             ('single', '<200f>עברית<200e>', 'id-142', '', None), ], 
    'doc5': [('single', '9-symbol', 'id-151', '', None),
             ('single', '&-symbol', 'id-152', '', None), ], 
    'doc6': [('single', '£100', 'id-161', '', None), ], 
}

testcase01o = []


#-------------------------------------------------------------------

class testIndexEntries(unittest.TestCase):
    def test01_special_letter(self):
        self.maxDiff = None
        env = util.env(testcase01i)
        bld = util.builder(env)
        gidx = util.IndexEntries(env).create_index(bld)
        self.assertEqual(testcase01o, gidx)

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
