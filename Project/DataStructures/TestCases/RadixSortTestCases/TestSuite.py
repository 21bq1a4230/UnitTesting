import unittest

import DataStructures.TestCases.RadixSortTestCases.RadixSortTestCases as rs


def RadixSuite():
    suite = unittest.TestSuite()
    suite.addTest(rs.RadixSortTestCases('test_1'))
    suite.addTest(rs.RadixSortTestCases('test_2'))
    suite.addTest(rs.RadixSortTestCases('test_3'))
    suite.addTest(rs.RadixSortTestCases('test_4'))
    suite.addTest(rs.RadixSortTestCases('test_5'))
    return suite


def TestRun():
    tester = unittest.TextTestRunner()
    tester.run(RadixSuite())
