class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def getListRev(self):
        val = self.head
        lt = []
        while val.next:
            val = val.next
        while val :
            lt.append(val.data)
            val = val.prev
        return lt

    def getList(self):
        val = self.head
        lt = []
        while val:
            lt.append(val.data)
        return lt

    def Insertion(self, data, pos):
        newNode = Node(data)
        if pos == "Head":
            if self.head is None:
                self.head = newNode
                return
            val = self.head
            newNode.next = val
            self.head = newNode
        elif pos == "END":
            if self.head is None:
                self.head = newNode
                return
            val = self.head
            while val.next:
                val = val.next
            val.next = newNode
            newNode.prev = val
        else:
            count = 1
            val = self.head
            while count != pos - 1:
                val = val.next
                count += 1
            newNode.next = val.next
            val.next.prev = newNode
            newNode.prev = val
            val.next = newNode

    def Deletion(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        val = self.head
        while val.data != data:
            val = val.next
        if val.next is None:
            val.prev.next = None
            return
        prevNode = val.prev
        nextNode = val.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def DeleteAtGivenPosition(self,pos):
        count = 1
        val = self.head
        while count != pos - 1:
            val = val.next
            count += 1
        temp = val.next
        val.next = temp.next
        temp.next.prev = val

    def getLength(self):
        count = 0
        val = self.head
        while val:
            val = val.next
            count+=1
        return count


if __name__ == "__main__":
    dll = DoublyLinkedList()
    lt = [8, 5, 9, 15, 14, 2, 12, 16, 17, 18, 11, 7, 20, 10, 19]
    for i in lt :
        dll.Insertion(i, "END")
    dll.Insertion(34, 9)
    print(dll.getList())

