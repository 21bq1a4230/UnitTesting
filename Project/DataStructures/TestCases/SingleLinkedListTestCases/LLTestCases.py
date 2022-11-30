import unittest
import DataStructures.DrivenCode.SingleLinkedList.main as ll


class Test(unittest.TestCase):
    def setUp(self):
        self.elements = []

    def test_1(self):
        self.ll1 = ll.SingleLinkedList()
        self.ll1.Insertion(2, "END")
        statement = "\n----------------------------------------------------------------------\nadded node : {}" \
                    "\nExpected : {} \n Actual : {}".format([2], [2], self.ll1.getList())
        self.assertEquals(self.ll1.getList(), [2], statement)

    def test_2(self):
        self.ll2 = ll.SingleLinkedList()
        lt = [19, 18, 14, 7, 16]
        for i in lt:
            self.ll2.Insertion(i, "END")
        self.ll2.Insertion(25, "HEAD")
        statement = "\n----------------------------------------------------------------------\n FAILED IN ADDING NODE " \
                    "AT HEAD \nadded nodes : {}" \
                    "\nExpected : {} \n Actual : {}".format([19, 18, 14, 7, 16], [25, 19, 18, 14, 7, 16],
                                                            self.ll2.getList())
        self.assertEquals(self.ll2.getList(), [25, 19, 18, 14, 7, 16], statement)

    def test_3(self):
        self.ll3 = ll.SingleLinkedList()
        lt = [7, 13, 12, 16, 20]
        for i in lt:
            self.ll3.Insertion(i, "END")
        self.ll3.Insertion(14, 4)
        statement = "\n----------------------------------------------------------------------\n FAILED IN ADDING NODE " \
                    "AT MIDDLE \nadded nodes : {}" \
                    "\nExpected : {} \n Actual : {}".format([7, 13, 12, 16, 20], [7, 13, 12, 14, 16, 20],
                                                            self.ll3.getList())
        self.assertEquals(self.ll3.getList(), [7, 13, 12, 14, 16, 20], statement)

    def test_4(self):
        self.ll4 = ll.SingleLinkedList()
        lt = [12, 19, 6, 14, 15, 13, 5, 3, 10, 17, 18, 11, 8, 2, 7, 16, 1, 4, 9, 20]
        for i in lt:
            self.ll4.Insertion(i, "END")
        self.ll4.Insertion(100, "END")
        statement = "\n----------------------------------------------------------------------\n FAILED IN ADDING NODE " \
                    "AT END \nadded nodes : {}" \
                    "\nExpected : {} \n Actual : {}".format(
            [12, 19, 6, 14, 15, 13, 5, 3, 10, 17, 18, 11, 8, 2, 7, 16, 1, 4, 9, 20],
            [12, 19, 6, 14, 15, 13, 5, 3, 10, 17, 18, 11, 8, 2, 7, 16, 1, 4, 9, 20, 100],
            self.ll4.getList())
        self.assertEquals(self.ll4.getList(),
                          [12, 19, 6, 14, 15, 13, 5, 3, 10, 17, 18, 11, 8, 2, 7, 16, 1, 4, 9, 20, 100]
                          , statement)

    def test_5(self):
        self.ll5 = ll.SingleLinkedList()
        lt = [9, 13, 14, 10, 5, 12, 8, 17, 11, 20, 7, 2, 6, 15, 4, 1, 3, 19, 18, 16]
        for i in lt:
            self.ll5.Insertion(i, "END")
        statement = "\n----------------------------------------------------------------------\n FAILED IN ADDING NODE " \
                    "AT MIDDLE \nadded nodes : {}" \
                    "\nExpected : {} \n Actual : {}".format(
            [9, 13, 14, 10, 5, 12, 8, 17, 11, 20, 7, 2, 6, 15, 4, 1, 3, 19, 18, 16], 20,
            self.ll5.length())
        self.assertEquals(self.ll5.length(), 20, statement)
