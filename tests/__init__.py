import unittest

from . import testcase01, testcase02, testcase03, testcase04, testcase05
from . import testcase11, testcase12, testcase13, testcase14
from . import testcase21, testcase31, testcase41
from . import testcase51, testcase52, testcase61, testcase71

def suites():
    suites = unittest.TestSuite()
    suites.addTests(unittest.makeSuite(testcase01.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase02.testEmpty))
    suites.addTests(unittest.makeSuite(testcase03.testSubterm))
    suites.addTests(unittest.makeSuite(testcase04.testIndexUnit))
    suites.addTests(unittest.makeSuite(testcase05.testIndexEntry))
    suites.addTests(unittest.makeSuite(testcase11.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase12.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase13.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase14.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase21.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase31.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase41.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase51.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase52.testIndexEntries))
    suites.addTests(unittest.makeSuite(testcase61.testXRefIndex))
    suites.addTests(unittest.makeSuite(testcase71.testBuilder))
    return suites
