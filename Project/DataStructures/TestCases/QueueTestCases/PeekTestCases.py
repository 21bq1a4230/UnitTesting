import unittest
import DataStructures.DrivenCode.Queue.Main as queue


class TestPeek(unittest.TestCase):
    def setUp(self):
        self.arr1 = ['a', 'e', 'i', 'o', 'u']
        self.enqueue2 = [2, 6, 3, 5, 9]

    def test_1(self):
        self.test1 = queue.Queue()
        for i in self.arr1:
            self.test1.Enqueue(i)
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Actual : {}".format(['a', 'e', 'i', 'o', 'u'], 'a', self.test1.peekRear())

        self.assertEquals(self.test1.peekEnd(), 'a', statement)

    def test_2(self):
        self.test1 = queue.Queue()
        for i in self.arr1:
            self.test1.Enqueue(i)
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Actual : {}".format(['a', 'e', 'i', 'o', 'u'], "u", self.test1.peekEnd())

        self.assertEquals(self.test1.peekRear(), "u", statement)

    def test_3(self):
        self.test2 = queue.Queue()
        for i in self.enqueue2:
            self.test2.Enqueue(i)
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Actual : {}".format([2, 6, 3, 5, 9], 2, self.test2.peekRear())

        self.assertEquals(self.test2.peekEnd(), 2, statement)

    def test_4(self):
        self.test2 = queue.Queue()
        for i in self.enqueue2:
            self.test2.Enqueue(i)
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Actual : {}".format([2, 6, 3, 5, 9], 9, self.test2.peekEnd())

        self.assertEquals(self.test2.peekRear(), 9, statement)


if __name__ == "__main__":
    unittest.main()
