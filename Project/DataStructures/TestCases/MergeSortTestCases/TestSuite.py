import unittest
import DataStructures.TestCases.MergeSortTestCases.testCases as tc


def MergeSortSuite():
    suite = unittest.TestSuite()
    suite.addTest(tc.MergeSortTest('test_1'))
    suite.addTest(tc.MergeSortTest('test_2'))
    suite.addTest(tc.MergeSortTest('test_3'))
    return suite


def TestRun():
    tester = unittest.TextTestRunner()
    tester.run(MergeSortSuite())
