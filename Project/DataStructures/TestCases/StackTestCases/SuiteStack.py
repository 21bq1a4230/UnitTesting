import unittest
import DataStructures.TestCases.StackTestCases.StackPeekTestCases as peek
import DataStructures.TestCases.StackTestCases.StackPushTestCases as push


def StackSuite():
    suite = unittest.TestSuite()
    suite.addTest(peek.ForPeek('test_1'))
    suite.addTest(peek.ForPeek('test_2'))
    suite.addTest(push.ForPush('test_1'))
    suite.addTest(push.ForPush('test_2'))
    return suite


def TestRun():
    tester = unittest.TextTestRunner()
    tester.run()