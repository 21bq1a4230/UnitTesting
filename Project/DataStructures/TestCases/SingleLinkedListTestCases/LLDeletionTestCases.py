import unittest
import DataStructures.DrivenCode.SingleLinkedList.main as ll


class Deletion(unittest.TestCase):
    def setUp(self):
        self.elements = []

    def test_1(self):
        self.ll1 = ll.SingleLinkedList()
        lt = [12, 19, 6, 14, 15, 13, 5, 3, 10, 17, 18, 11, 8, 2, 7, 16, 1, 4, 9, 20]
        for i in lt:
            self.ll1.Insertion(i, "END")
        self.ll1.Deletion(10)
        statement = "FAILED IN NODE DELETION \n NODES PUSH {} \n EXPECTED : {} \n ACTUAL : {} ".format(lt,
                                                                                                       [12, 19, 6, 14,
                                                                                                        15, 13, 5, 3,
                                                                                                        17, 18, 11,
                                                                                                        8, 2, 7, 16, 1,
                                                                                                        4, 9, 20],
                                                                                                       self.ll1.getList())
        self.assertEquals(self.ll1.getList(), [12, 19, 6, 14, 15, 13, 5, 3, 17, 18, 11, 8, 2, 7, 16, 1, 4, 9, 20],
                          statement)

    def test_2(self):
        self.ll2 = ll.SingleLinkedList()
        lt = [12, 19, 6, 14, 15, 13, 5, 3, 10, 17, 18, 11, 8, 2, 7, 16, 1, 4, 9, 20]
        for i in lt:
            self.ll2.Insertion(i, "END")
        self.ll2.Deletion(0)
        statement = "FAILED IN NODE DELETION \n NODES PUSH {} \n EXPECTED : {} \n ACTUAL : {} ".format(lt, -1,
                                                                                                       self.ll2.Deletion(
                                                                                                           0))
        self.assertEquals(self.ll2.Deletion(0), -1, statement)

    def test_3(self):
        self.ll3 = ll.SingleLinkedList()
        lt = [67227, 12957, 69140, 65311, 92006, 96328, 69898, 59912, 81897, 6122, 81409, 72242, 21108, 54188, 60106]
        for i in lt:
            self.ll3.Insertion(i, "END")
        self.ll3.DeleteNodeAtGivenPosition(10)
        statement = "FAILED IN DELETION AT A GIVEN POSITION \n NODES : {} \n , EXPECTED : {} \n ACTUAL : {} ".format(lt,
                                                                                                                     [
                                                                                                                         67227,
                                                                                                                         12957,
                                                                                                                         69140,
                                                                                                                         65311,
                                                                                                                         92006,
                                                                                                                         96328,
                                                                                                                         69898,
                                                                                                                         59912,
                                                                                                                         81897,
                                                                                                                         6122,
                                                                                                                         72242,
                                                                                                                         21108,
                                                                                                                         54188,
                                                                                                                         60106],
                                                                                                                     self.ll3.getList())
        self.assertEquals(self.ll3.getList(),
                          [67227, 12957, 69140, 65311, 92006, 96328, 69898, 59912, 81897, 6122, 72242, 21108, 54188,
                           60106], statement)

    def test_4(self):
        self.ll4 = ll.SingleLinkedList()
        lt = [60457, 869, 92230, 22371, 68213, 51591, 72201, 81335, 84496, 87444, 26168, 3340, 440, 86559, 78484]
        for i in lt:
            self.ll4.Insertion(i, "END")
        self.ll4.DeleteNodeAtGivenPosition(99)
        statement = "FAILED IN DELETION AT A GIVEN POSITION \n NODES : {}\nEXPECTED : {}\nACTUAL : {}".format(lt, -1,
                                                                                                              self.ll4.Deletion(
                                                                                                                  99))
        self.assertEquals(-1, self.ll4.Deletion(99), statement)
