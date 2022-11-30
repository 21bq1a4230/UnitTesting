import unittest
import DataStructures.TestCases.BinarySearchTestCases.BinarysearchTestCases as bst


def BinarySearchSuite():
    suite = unittest.TestSuite()
    suite.addTest(bst.BinarySearchTest('test_1'))
    suite.addTest(bst.BinarySearchTest('test_2'))
    suite.addTest(bst.BinarySearchTest('test_3'))
    suite.addTest(bst.BinarySearchTest('test_4'))
    suite.addTest(bst.BinarySearchTest('test_5'))
    return suite


def TestRun():
    tester = unittest.TextTestRunner()
    tester.run(BinarySearchSuite())
