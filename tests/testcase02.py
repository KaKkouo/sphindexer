#!/usr/bin/python
import unittest
from src import rack

#-------------------------------------------------------------------

class testEmpty(unittest.TestCase):
    def test01_repr(self):
        emp = rack.Empty()
        self.assertEqual('<#empty>', repr(emp))
    def test02_str(self):
        emp = rack.Empty()
        self.assertEqual('', str(emp))
    def test03_bool(self):
        emp = rack.Empty()
        self.assertEqual(False, bool(emp))

#-------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
