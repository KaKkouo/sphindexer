#!/usr/bin/python
import unittest
from docutils.nodes import Text as txt
from src import rack

repr00 = "<Subterm: len=2 <#text: 'sphinx'><#text: 'python'>>"
repr01 = "<IndexUnit: main='main' file_name='doc1' target='term-1' <#empty><#text: 'docutils'><Subterm: len=2 <#text: 'sphinx'><#text: 'python'>>>"

#-------------------------------------------------------------------

class testIndexUnit(unittest.TestCase):
    def test01_repr(self):
        pack = rack.Subterm('3', txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', 'main', 'doc1', 'term-1', 'clsf')
        self.assertEqual(repr00, repr(pack))
        self.assertEqual(repr01, repr(unit))

    def test02_dict(self):
        pack = rack.Subterm('3', txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', 'main', 'doc1', 'term-1', 'clsf')
        self.assertEqual('main', unit['main'])
        self.assertEqual('doc1', unit['file_name'])
        self.assertEqual('term-1', unit['target'])
        self.assertEqual('clsf', unit['index_key'])

    def test03_list(self):
        pack = rack.Subterm('3', txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', 'main', 'doc1', 'term-1', 'clsf')
        self.assertEqual("<#empty>", repr(unit[0]))
        self.assertEqual("<#text: 'docutils'>", repr(unit[1]))
        self.assertEqual(repr00, repr(unit[2]))
        self.assertEqual("main", unit[3])
        unit[0] = txt(unit['index_key'])
        unit[1] = txt(unit[1])
        unit[2] = rack.Subterm('3', txt('sphinx'), txt('python'))
        self.assertEqual("<#text: 'clsf'>", repr(unit[0]))
        self.assertEqual("<#text: 'docutils'>", repr(unit[1]))
        self.assertEqual(repr00, repr(unit[2]))

    def test04_get_children(self):
        pack = rack.Subterm('3', txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', 'main', 'doc1', 'term-1', 'clsf')
        self.assertEqual(['docutils', 'sphinx', 'python'], unit.get_children())

    def test05_set_sbtm_delimiter(self):
        pack = rack.Subterm('3', txt('sphinx'), txt('python'))
        unit = rack.IndexUnit(txt('docutils'), pack, '2', 'main', 'doc1', 'term-1', 'clsf')
        self.assertEqual(['docutils', 'sphinx', 'python'], unit.astexts())
        unit.set_subterm_delimiter()
        self.assertEqual('sphinx, python', unit[2].astext())

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
