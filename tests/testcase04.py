#!/usr/bin/python
import unittest
from docutils.nodes import Text as txt
from src import rack

repr00 = "<Subterm: len=2 <#text: 'sphinx'><#text: 'python'>>"
repr01 = "<IndexUnit: main file_name='doc1' target='term-1' <#text: ''><#text: 'docutils'><Subterm: len=2 <#text: 'sphinx'><#text: 'python'>>>"
repr02 = "<IndexUnit: main file_name='doc1' target='term-1' <#text: 'clsf'><#text: 'docutils'><Subterm: len=2 <#text: 'sphinx'><#text: 'python'>>>"

#-------------------------------------------------------------------

main = "3"

class testIndexUnit(unittest.TestCase):
    def test01_repr(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        self.assertEqual(repr00, repr(pack))
        self.assertEqual(repr01, repr(unit))

    def test02_repr(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        unit[0] = txt(unit['index_key'])
        self.assertEqual(repr02, repr(unit))

    def test03_dict(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        self.assertEqual(main, unit['main'])
        self.assertEqual('doc1', unit['file_name'])
        self.assertEqual('term-1', unit['target'])
        self.assertEqual('clsf', unit['index_key'])

    def test04_list(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        self.assertEqual("<#text: ''>", repr(unit[0]))
        self.assertEqual("<#text: 'docutils'>", repr(unit[1]))
        self.assertEqual(repr00, repr(unit[2]))
        self.assertEqual(main, unit['main'])
        unit[0] = txt(unit['index_key'])
        unit[1] = txt(unit[1])
        unit[2] = rack.Subterm(main, txt('sphinx'), txt('python'))
        self.assertEqual("<#text: 'clsf'>", repr(unit[0]))
        self.assertEqual("<#text: 'docutils'>", repr(unit[1]))
        self.assertEqual(repr00, repr(unit[2]))

    def test06_set_sbtm_delimiter(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        self.assertEqual(['docutils', 'sphinx', 'python'], unit.astexts())
        unit.set_subterm_delimiter()
        self.assertEqual('sphinx, python', unit[2].astext())

    def test07_raise(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        with self.assertRaises(KeyError):
            a = unit['forbar']

    def test08_raise(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        with self.assertRaises(IndexError):
            a = unit[99]

    def test09_raise(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        with self.assertRaises(TypeError):
            a = unit[(99,'a')]

    def test10_raise(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        with self.assertRaises(AttributeError):
            unit[99] = 1

    def test11_raise(self):
        pack = rack.Subterm(main, txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', main, 'doc1', 'term-1', 'clsf')
        with self.assertRaises(TypeError):
            unit[(99,'a')] = 1

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
