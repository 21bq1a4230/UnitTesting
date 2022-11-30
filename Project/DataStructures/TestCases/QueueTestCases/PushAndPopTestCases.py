import unittest
import DataStructures.DrivenCode.Queue.Main as queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.enqueue1 = ['a', 'e', 'i', 'o', 'u']
        self.enqueue2 = [2, 6, 3, 5, 9]
        self.enqueue3 = []
        self.result = []

    def test_1(self):
        self.result = []
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Actual : {}".format(['a', 'e', 'i', 'o', 'u'], ['a', 'e', 'i', 'o', 'u'],
                                                            self.result)
        self.test1 = queue.Queue()
        for i in self.enqueue1:
            self.test1.Enqueue(i)
        for j in range(len(self.enqueue1)):
            self.result.append(self.test1.DeQueue())
        self.assertEquals(['a', 'e', 'i', 'o', 'u'], self.result, statement)

    def test_2(self):
        self.result = []
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Actual : {}".format([2, 6, 3, 5, 9], [2, 6, 3, 5, 9],
                                                            self.result)
        self.test2 = queue.Queue()
        for i in self.enqueue2:
            self.test2.Enqueue(i)
        for i in range(len(self.enqueue2)):
            self.result.append(self.test2.DeQueue())
        self.assertEquals([2, 6, 3, 5, 9], self.result, statement)


if __name__ == "__main__":
    unittest.main()
