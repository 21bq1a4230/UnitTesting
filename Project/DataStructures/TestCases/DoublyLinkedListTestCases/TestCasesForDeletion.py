from random import randint, choice
import unittest
import DataStructures.DrivenCode.DoublyLinkedList.main as dl


class TestCases(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        dll = dl.DoublyLinkedList()
        lt = []
        for i in range(randint(1, 20)):
            lt.append(randint(1, 100))
        r = choice(lt)
        for i in lt:
            dll.Insertion(i, "END")
        dll.Deletion(r)
        ltr = lt.remove(r)
        statement = "FAILED\nNODES PUSHED : {}\nREMOVED : {}\nEXPECTED : {}\nACTUAL : {}".format(lt, r, ltr,
                                                                                                 dll.getList())
        self.assertEquals(ltr, dll.getListRev(), statement)

    def test_2(self):
        dll = dl.DoublyLinkedList()
        lt = []
        for i in range(randint(1, 20)):
            lt.append(randint(1, 100))
        r = choice(range(len(lt)))
        for i in lt:
            dll.Insertion(i, "End")
        dll.DeleteAtGivenPosition(r)
        ltr = lt.remove(lt[r])
        statement = "FAILED\nNODES PUSHED : {}\nREMOVED : {}\nEXPECTED : {}\nACTUAL : {}".format(lt, lt[r], ltr,
                                                                                                 dll.getList())
        self.assertEquals(ltr, dll.getListRev(), statement)

    def test_3(self):
        dll = dl.DoublyLinkedList()
        lt = []
        for i in range(randint(1, 20)):
            lt.append(randint(1, 100))
        for i in lt:
            dll.Insertion(i, "End")
        ltr = lt[::-1]
        statement = "FAILED\nNODES PUSHED : {}\nEXPECTED : {}\nACTUAL : {}".format(lt, ltr, dll.getListRev())
        self.assertEquals(ltr, dll.getListRev(), statement)
