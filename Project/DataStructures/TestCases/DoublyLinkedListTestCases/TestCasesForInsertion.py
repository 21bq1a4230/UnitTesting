from random import randint
import unittest
import DataStructures.DrivenCode.DoublyLinkedList.main as dl


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.dll1 = dl.DoublyLinkedList()
        lt = [3, 7, 1, 20, 5, 13, 16, 17, 2, 9, 10, 14, 11, 8, 6]
        for i in lt:
            self.dll1.Insertion(i, "End")
        self.dll1.Insertion(56, "Head")
        statment = "FAILED \n NODES INSERTED : {} and {}\nEXPECTED : {}\nACTUAL : {}".format(lt, [56],
                                                                                             [56, 3, 7, 1, 20, 5, 13,
                                                                                              16, 17, 2, 9, 10, 14, 11,
                                                                                              8, 6],
                                                                                             self.dll1.getList())
        self.assertEquals(self.dll1.getList(), [56, 3, 7, 1, 20, 5, 13, 16, 17, 2, 9, 10, 14, 11, 8, 6], statment)

    def test_2(self):
        self.dll2 = dl.DoublyLinkedList()
        lt = [8, 5, 9, 15, 14, 2, 12, 16, 17, 18, 11, 7, 20, 10, 19]
        for i in lt:
            self.dll2.Insertion(i, "End")
        self.dll2.Insertion(34, 9)
        statment = "FAILED \n NODES INSERTED : {} and {}\nEXPECTED : {}\nACTUAL : {}".format(lt, 34,
                                                                                             [8, 5, 9, 15, 14, 2, 12,
                                                                                              16, 34, 17, 18, 11, 7, 20,
                                                                                              10, 19],
                                                                                             self.dll2.getList())
        self.assertEquals(self.dll2.getList(), [8, 5, 9, 15, 14, 2, 12, 16, 34, 17, 18, 11, 7, 20, 10, 19])

    def test_3(self):
        self.dll3 = dl.DoublyLinkedList()
        lt = [6, 19, 1, 17, 12, 15, 2, 7, 5, 16, 14, 18, 13, 3, 20]
        for i in lt:
            self.dll3.Insertion(i, "Head")
        self.dll3.Insertion(3, "End")
        statement = "FAILED \n NODES INSERTED : {} AND {} \nEXPECTED : {}\nACTUAL : {}".format(lt, 3,
                                                                                               [6, 19, 1, 17, 12, 15, 2,
                                                                                                7, 5, 16, 14, 18, 13, 3,
                                                                                                20, 3],
                                                                                               self.dll3.getList())
        self.assertEquals(self.dll3.getList(), [6, 19, 1, 17, 12, 15, 2, 7, 5, 16, 14, 18, 13, 3, 20, 3], statement)

    def test_4(self):
        self.dll4 = dl.DoublyLinkedList()
        lt = []
        for i in range(randint(1, 20)):
            lt.append(randint(1, 100))
        for i in lt:
            self.dll4.Insertion(i, "End")
        l = self.dll4.getLength()
        statement = "FAILED \n NODES INSERTED : {} LENGTH EXPECTED : {}\nACTUAL : {}".format(lt, len(lt), l)
        self.assertEquals(l, len(lt),statement)
