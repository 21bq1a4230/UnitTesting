import unittest
import DataStructures.TestCases.QuickSortTestCases.testCases as tc


def InsertionSortSuite():
    suite = unittest.TestSuite()
    suite.addTest(tc.QuickSortTest('test_1'))
    suite.addTest(tc.QuickSortTest('test_2'))
    suite.addTest(tc.QuickSortTest('test_3'))
    return suite


def TestRun():
    tester = unittest.TextTestRunner()
    tester.run(InsertionSortSuite())
