import unittest
import DataStructures.TestCases.QueueTestCases.PeekTestCases as peekTest
import DataStructures.TestCases.QueueTestCases.PushAndPopTestCases as pushTest


def QueueStack():
    suite = unittest.TestSuite()
    suite.addTest(peekTest.TestPeek('test_1'))
    suite.addTest(peekTest.TestPeek('test_2'))
    suite.addTest(peekTest.TestPeek('test_3'))
    suite.addTest(peekTest.TestPeek('test_4'))
    suite.addTest(pushTest.TestQueue('test_1'))
    suite.addTest(pushTest.TestQueue('test_2'))
    return suite


def RunTest():
    tester = unittest.TextTestRunner()
    tester.run(QueueStack())
