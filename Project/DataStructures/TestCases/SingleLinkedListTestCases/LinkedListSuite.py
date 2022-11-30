import unittest
import DataStructures.TestCases.SingleLinkedListTestCases.LLTestCases as tests1
import DataStructures.TestCases.SingleLinkedListTestCases.LLDeletionTestCases as test2


def Suite():
    suite = unittest.TestSuite()
    suite.addTest(tests1.Test('test_1'))
    suite.addTest(tests1.Test('test_2'))
    suite.addTest(tests1.Test('test_3'))
    suite.addTest(tests1.Test('test_4'))
    suite.addTest(tests1.Test('test_5'))
    suite.addTest(test2.Deletion('test_4'))
    suite.addTest(test2.Deletion('test_3'))
    suite.addTest(test2.Deletion('test_2'))
    suite.addTest(test2.Deletion('test_1'))
    return suite


def TestRun():
    tester = unittest.TextTestRunner()
    tester.run(Suite())
