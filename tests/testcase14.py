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

testcase01o = [
('Symbols',
  [('&-symbol', [[('', 'doc5.html#id-152')], [], None]),
   ('9-symbol', [[('', 'doc5.html#id-151')], [], None]),
   ('<200f>עברית<200e>', [[('', 'doc4.html#id-142')], [], None]),
   ('£100', [[('', 'doc6.html#id-161')], [], None])]),
 ('D',
  [('docutils', [[('', 'doc1.html#id-111')], [], None])]),
 ('P',
  [('pip',
    [[],
     [('install', [('', 'doc2.html#id-121')]),
      ('upgrade', [('', 'doc2.html#id-122')])],
     None]),
   ('Python', [[('', 'doc1.html#id-112')], [], None])]),
 ('S', [('Sphinx', [[('', 'doc3.html#id-131')], [], None])]),
 ('Е',
  [('ёлка', [[('', 'doc4.html#id-141')], [], None]),
   ('Ель', [[('', 'doc3.html#id-132')], [], None])])
]


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
