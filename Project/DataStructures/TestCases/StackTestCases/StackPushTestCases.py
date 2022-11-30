import unittest
import DataStructures.DrivenCode.Stack.main as stk


class ForPush(unittest.TestCase):
    def setUp(self):
        self.pushingArray1 = [2, 5, 4, 3, 6]
        self.pushingArray2 = ['a', 'e', 'i', 'o', 'u']
        self.lt = []

    def test_1(self):
        self.lt = []
        self.test1 = stk.Stack()
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Acutal : {}".format([2, 5, 4, 3, 6],[6, 3, 4, 5, 2], self.lt)
        for i in self.pushingArray1:
            self.test1.push(i)
        for i in self.pushingArray1:
            self.lt.append(self.test1.pop())
        self.assertEquals(self.lt, [6, 3, 4, 5, 2], statement)

    def test_2(self):
        self.lt = []
        self.test2 = stk.Stack()
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Acutal : {}".format(['a', 'e', 'i', 'o', 'u'],['u', 'o', 'i', 'e', 'a'],
                                                            self.lt)
        for i in self.pushingArray2:
            self.test2.push(i)
        for i in self.pushingArray2:
            self.lt.append(self.test2.pop())
        self.assertEquals(self.lt, ['u', 'o', 'i', 'e', 'a'], statement)


if __name__ == "__main__":
    unittest.main()
