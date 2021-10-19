import unittest

from . import testcase01

def suites():
    suites = unittest.TestSuite()
    suites.addTests(unittest.makeSuite(testcase01.testIndexEntries))
    return suites
