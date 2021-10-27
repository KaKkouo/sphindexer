#!/usr/bin/python
import unittest
from docutils import nodes
from src import rack

#-------------------------------------------------------------------

class testSubterm(unittest.TestCase):
    def test01_no_Text(self):
        pack = rack.Subterm('5')
        self.assertEqual('', str(pack))
        self.assertEqual('<Subterm: len=0 >', repr(pack))
        self.assertEqual(True, pack == '')

    def test02_no_Text(self):
        pack = rack.Subterm('8')
        self.assertEqual('', str(pack))
        self.assertEqual("<Subterm: len=0 tpl='see %s' >", repr(pack))
        self.assertEqual(True, pack == '')

    def test03_no_Text(self):
        pack = rack.Subterm('9')
        self.assertEqual('', str(pack))
        self.assertEqual("<Subterm: len=0 tpl='see also %s' >", repr(pack))
        self.assertEqual(True, pack == '')

    def test11_one_Text(self):
        pack = rack.Subterm('5', nodes.Text('sphinx'))
        self.assertEqual('sphinx', str(pack))
        self.assertEqual("<Subterm: len=1 <#text: 'sphinx'>>", repr(pack))
        self.assertEqual(True, pack == 'sphinx')

    def test12_one_Text(self):
        pack = rack.Subterm('8', nodes.Text('sphinx'))
        self.assertEqual('see sphinx', str(pack))
        self.assertEqual("<Subterm: len=1 tpl='see %s' <#text: 'sphinx'>>", repr(pack))
        self.assertEqual(True, pack == 'see sphinx')

    def test21_one_Text(self):
        pack = rack.Subterm('5', nodes.Text('sphinx'), nodes.Text('python'))
        self.assertEqual('sphinx python', str(pack))
        self.assertEqual("<Subterm: len=2 <#text: 'sphinx'><#text: 'python'>>", repr(pack))
        self.assertEqual(True, pack == 'sphinx python')
        pack.set_delimiter(', ')
        self.assertEqual('sphinx, python', str(pack))

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
