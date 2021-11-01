#!/usr/bin/python
import unittest
from docutils.nodes import Text as txt
from src import rack

head01 = "<IndexEntry: entry_type='single'"
attr01 = "main='main' file_name='doc1' target='term-1' index_key='key'"
repr01 = f"{head01} {attr01} <#text: 'sphinx'>>"

repr010 = "<IndexUnit: main file_name='doc1' target='term-1' <#empty><#text: 'sphinx'>>"

head02 = "<IndexEntry: entry_type='single'"
attr02 = "main='main' file_name='doc1' target='term-1' index_key='key'"
repr02 = f"{head02} {attr02} <#text: 'sphinx'><#text: 'python'>>"

head020 = "<IndexUnit: main file_name='doc1' target='term-1'"
pack020 = "<Subterm: len=1 <#text: 'python'>>"
repr020 = f"{head020} <#empty><#text: 'sphinx'>{pack020}>"

head03 = "<IndexEntry: entry_type='pair'"
attr03 = "main='main' file_name='doc1' target='term-1' index_key='key'"
repr03 = f"{head03} {attr03} <#text: 'sphinx'><#text: 'python'>>"

head030 = "<IndexUnit: main file_name='doc1' target='term-1'"
pack030 = "<Subterm: len=1 <#text: 'python'>>"
repr030 = f"{head030} <#empty><#text: 'sphinx'>{pack030}>"

head031 = "<IndexUnit: main file_name='doc1' target='term-1'"
pack031 = "<Subterm: len=1 <#text: 'sphinx'>>"
repr031 = f"{head031} <#empty><#text: 'python'>{pack031}>"

head04 = "<IndexEntry: entry_type='triple'"
attr04 = "main='main' file_name='doc1' target='term-1' index_key='key'"
repr04 = f"{head04} {attr04} <#text: 'docutils'><#text: 'sphinx'><#text: 'python'>>"

head040 = "<IndexUnit: main file_name='doc1' target='term-1'"
pack040 = "<Subterm: len=2 <#text: 'sphinx'><#text: 'python'>>"
repr040 = f"{head040} <#empty><#text: 'docutils'>{pack040}>"

head041 = "<IndexUnit: main file_name='doc1' target='term-1'"
pack041 = "<Subterm: len=2 delimiter=', ' <#text: 'python'><#text: 'docutils'>>"
repr041 = f"{head041} <#empty><#text: 'sphinx'>{pack041}>"

head042 = "<IndexUnit: main file_name='doc1' target='term-1'"
pack042 = "<Subterm: len=2 <#text: 'docutils'><#text: 'sphinx'>>"
repr042 = f"{head042} <#empty><#text: 'python'>{pack042}>"

head05 = "<IndexEntry: entry_type='see'"
attr05 = "main='main' file_name='doc1' target='term-1' index_key='key'"
repr05 = f"{head05} {attr05} <#text: 'sphinx'><#text: 'python'>>"

head050 = "<IndexUnit: main file_name='doc1' target='term-1'"
pack050 = "<Subterm: len=1 tpl='see %s' <#text: 'python'>>"
repr050 = f"{head050} <#empty><#text: 'sphinx'>{pack050}>"

head06 = "<IndexEntry: entry_type='seealso'"
attr06 = "main='main' file_name='doc1' target='term-1' index_key='key'"
repr06 = f"{head06} {attr06} <#text: 'sphinx'><#text: 'python'>>"

head060 = "<IndexUnit: main file_name='doc1' target='term-1'"
pack060 = "<Subterm: len=1 tpl='see also %s' <#text: 'python'>>"
repr060 = f"{head060} <#empty><#text: 'sphinx'>{pack060}>"

head07 = "<IndexEntry: entry_type='list'"
attr07 = "main='main' file_name='doc1' target='term-1' index_key='key'"
repr07 = f"{head07} {attr07} <#text: 'docutils'><#text: 'sphinx'><#text: 'python'>>"

repr070 = "<IndexUnit: main file_name='doc1' target='term-1' <#empty><#text: 'docutils'>>"

head08 = "<IndexEntry: entry_type='foobar'"
attr08 = "main='main' file_name='doc1' target='term-1' index_key='key'"
repr08 = f"{head08} {attr08} <#text: 'docutils'><#text: 'sphinx'><#text: 'python'>>"

repr080 = "<IndexUnit: main file_name='doc1' target='term-1' <#empty><#text: 'docutils'>>"

#-------------------------------------------------------------------

main = "3"

class testIndexEntry(unittest.TestCase):
    def test01_single_one(self):
        entry = rack.IndexEntry('sphinx', 'single', 'doc1', 'term-1', 'main', 'key')
        self.assertEqual(repr01, repr(entry))
        self.assertEqual("sphinx", entry.astext())
        units = entry.make_index_units()
        self.assertEqual(repr010, repr(units[0]))

    def test02_single_two(self):
        entry = rack.IndexEntry('sphinx; python', 'single', 'doc1', 'term-1', 'main', 'key')
        self.assertEqual(repr02, repr(entry))
        self.assertEqual("sphinx; python", entry.astext())
        units = entry.make_index_units()
        self.assertEqual(repr020, repr(units[0]))

    def test03_pair(self):
        entry = rack.IndexEntry('sphinx; python', 'pair', 'doc1', 'term-1', 'main', 'key')
        self.assertEqual(repr03, repr(entry))
        self.assertEqual("sphinx; python", entry.astext())
        units = entry.make_index_units()
        self.assertEqual(repr030, repr(units[0]))
        self.assertEqual(repr031, repr(units[1]))

    def test04_triple(self):
        value = 'docutils; sphinx; python'
        entry = rack.IndexEntry(value, 'triple', 'doc1', 'term-1', 'main', 'key')
        self.assertEqual(repr04, repr(entry))
        self.assertEqual("docutils; sphinx; python", entry.astext())
        units = entry.make_index_units()
        self.assertEqual(repr040, repr(units[0]))
        self.assertEqual(repr041, repr(units[1]))
        self.assertEqual(repr042, repr(units[2]))

    def test05_see(self):
        entry = rack.IndexEntry('sphinx; python', 'see', 'doc1', 'term-1', 'main', 'key')
        self.assertEqual(repr05, repr(entry))
        self.assertEqual("sphinx; python", entry.astext())
        units = entry.make_index_units()
        self.assertEqual(repr050, repr(units[0]))

    def test06_seealso(self):
        entry = rack.IndexEntry('sphinx; python', 'seealso', 'doc1', 'term-1', 'main', 'key')
        self.assertEqual(repr06, repr(entry))
        self.assertEqual("sphinx; python", entry.astext())
        units = entry.make_index_units()
        self.assertEqual(repr060, repr(units[0]))

    def test07_other(self):
        value = 'docutils; sphinx; python'
        entry = rack.IndexEntry(value, 'list', 'doc1', 'term-1', 'main', 'key')
        self.assertEqual(repr07, repr(entry))
        self.assertEqual("docutils; sphinx; python", entry.astext())
        units = entry.make_index_units()
        self.assertEqual(repr070, repr(units[0]))

    def test08_other(self):
        value = 'docutils; sphinx; python'
        entry = rack.IndexEntry(value, 'foobar', 'doc1', 'term-1', 'main', 'key')
        self.assertEqual(repr08, repr(entry))
        self.assertEqual("docutils; sphinx; python", entry.astext())
        units = entry.make_index_units()
        with self.assertRaises(IndexError):
            a = repr(units[0])

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
