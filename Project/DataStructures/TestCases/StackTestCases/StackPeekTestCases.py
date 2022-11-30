import unittest
import DrivenCode.Stack.main as stk


class ForPeek(unittest.TestCase):
    def setUp(self):
        self.arr = [2, 5, 4, 3]

    def test_1(self):
        self.test1 = stk.Stack()
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Acutal : {}".format("none", None, self.test1.peek())
        self.assertEquals(self.test1.peek(), None, statement)

    def test_2(self):
        self.test2 = stk.Stack()
        statement = "\n----------------------------------------------------------------------\npushed : {}" \
                    "\nExpected : {} \n Acutal : {}".format(self.arr, 3, self.test2.peek())
        for i in self.arr:
            self.test2.push(i)

        self.assertEquals(self.test2.peek(), 3, statement)


if __name__ == "__main__":
    unittest.main()
