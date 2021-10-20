import unittest

from . import testcase01, testcase02, testcase03, testcase04, testcase05

def suites():
    suites = unittest.TestSuite()
    suites.addTests(unittest.makeSuite(testcase01.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase02.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase03.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase04.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase05.testIndexEntries))
    return suites
