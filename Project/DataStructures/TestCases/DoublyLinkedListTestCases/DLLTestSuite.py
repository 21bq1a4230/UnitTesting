import unittest
import DataStructures.TestCases.DoublyLinkedListTestCases.TestCasesForDeletion as delTest
import DataStructures.TestCases.DoublyLinkedListTestCases.TestCasesForInsertion as insTest


def SuiteFunc():
    suite = unittest.TestSuite()
    suite.addTest(delTest.TestCases('test_1'))
    suite.addTest(delTest.TestCases('test_3'))
    suite.addTest(delTest.TestCases('test_2'))
    suite.addTest(insTest.Test('test_1'))
    suite.addTest(insTest.Test('test_2'))
    suite.addTest(insTest.Test('test_3'))
    suite.addTest(insTest.Test('test_4'))
    return suite

def TestRun():
    tester = unittest.TextTestRunner()
    tester.run(SuiteFunc())

if __name__ == "__main__":
    pass