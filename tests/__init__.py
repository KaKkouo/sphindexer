import unittest

from . import testcase01, testcase02    

def suites():
    suites = unittest.TestSuite()
    suites.addTests(unittest.makeSuite(testcase01.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase02.testIndexEntries))
    return suites
