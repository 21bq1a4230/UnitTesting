import unittest
import DataStructures.DrivenCode.BinarySearch.main as bs


class BinarySearchTest(unittest.TestCase):
    def setUp(self):
        self.test1 = bs.BinarySearch(arr=[1, 2, 3, 5, 7, 8, 10, 11, 17, 20], x=10)
        self.test2 = bs.BinarySearch(arr=[1, 2, 3, 5, 7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20], x=20)
        self.test3 = bs.BinarySearch(arr=[11, 2, 12, 19, 4, 8, 5, 16, 20, 3, 14, 18, 9, 15, 10], x=15)
        self.test4 = bs.BinarySearch(arr=[2, 6, 8, 9, 10, 11, 12, 15, 15, 16, 17, 19, 20], x=15)
        self.test5 = bs.BinarySearch(arr=[1, 2, 3, 5, 6, 7, 8, 12, 13, 14, 16, 17, 19], x=100)

    def test_1(self):
        statement = "\n----------------------------------------------------------------------\narray : {}\nkey :" \
                    " {}\nExpected : {} \n Actual : {}".format([1, 2, 3, 5, 7, 8, 10, 11, 17, 20], 10, 7, self.test1)
        self.assertEquals(self.test1, 7, statement)

    def test_2(self):
        statement = "\n----------------------------------------------------------------------\narray : {}\nkey :" \
                    " {}\nExpected : {} \n Actual : {}".format([1, 2, 3, 5, 7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20],
                                                               20, 15, self.test2)
        self.assertEquals(self.test2, 15, statement)

    def test_3(self):
        statement = "\n----------------------------------------------------------------------\narray : {}\nkey :" \
                    " {}\nExpected : {} \n Actual : {}".format([11, 2, 12, 19, 4, 8, 5, 16, 20, 3, 14, 18, 9, 15, 10],
                                                               15, -1, self.test3)
        self.assertEquals(self.test3, -1, statement)

    def test_4(self):
        statement = "\n----------------------------------------------------------------------\narray : {}\nkey :" \
                    " {}\nExpected : {} \n Actual : {}".format([2, 6, 8, 9, 10, 11, 12, 15, 15, 16, 17, 19, 20], 15, 8,
                                                               self.test4)

        self.assertEquals(self.test4, 8, statement)

    def test_5(self):
        statement = "\n----------------------------------------------------------------------\narray : {}\nkey :" \
                    " {}\nExpected : {} \n Actual : {}".format([1, 2, 3, 5, 6, 7, 8, 12, 13, 14, 16, 17, 19], 100, -1,
                                                               self.test5)

        self.assertEquals(self.test5, -1, statement)


if __name__ == "__main__":
    unittest.main()
