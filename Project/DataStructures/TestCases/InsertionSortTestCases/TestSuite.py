import unittest
import DataStructures.TestCases.RadixSortTestCases.RadixSortTestCases as tc


def RadixSortSuite():
    suite = unittest.TestSuite()
    suite.addTest(tc.RadixSortTestCases('test_1'))
    suite.addTest(tc.RadixSortTestCases('test_2'))
    suite.addTest(tc.RadixSortTestCases('test_3'))
    suite.addTest(tc.RadixSortTestCases('test_4'))
    suite.addTest(tc.RadixSortTestCases('test_5'))
    return suite


def TestRun():
    tester = unittest.TextTestRunner()
    tester.run(RadixSortSuite())
