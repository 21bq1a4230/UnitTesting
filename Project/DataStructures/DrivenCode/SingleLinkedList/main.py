class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def getList(self):
        val = self.head
        lt = []
        while val:
            lt.append(val.data)
            val = val.next
        return lt

    def getNode(self, data):
        val = self.head
        while val.data != data:
            val = val.next
        return val

    def Insertion(self, data, pos):
        newNode = Node(data)
        if pos == "HEAD":
            newNode.next = self.head
            self.head = newNode
        elif pos == "END":
            if self.head is None:
                self.head = newNode
                return
            val = self.head
            while val.next is not None:
                val = val.next
            val.next = newNode
        else:
            count = 1
            val = self.head
            while count != pos - 1:
                val = val.next
                count += 1
            newNode.next = val.next
            val.next = newNode

    def length(self):
        count = 0
        val = self.head
        while val:
            val = val.next
            count += 1
        return count

    def Deletion(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        val = self.head
        while val.next.data != data:
            val = val.next
            if val.next is None:
                return -1
        val.next = val.next.next

    def DeleteNodeAtGivenPosition(self, pos):
        count = 0
        if pos > self.length():
            return -1
        if pos == 1:
            self.head = self.head.next
        val = self.head
        while count != pos - 1:
            val = val.next
            count += 1
        val.next = val.next.next


if __name__ == "__main__":
    sll = SingleLinkedList()
    lt = [67227, 12957, 69140, 65311, 92006, 96328, 69898, 59912, 81897, 6122, 81409, 72242, 21108, 54188, 60106]
    for i in lt:
        sll.Insertion(i, "END")
    # print(sll.getList())
    # sll.Insertion(24, 3)
    # print(sll.getList())
    # sll.Insertion(161198, "END")
    # print(sll.getList())
    # sll.Insertion(26, "HEAD")
    print(sll.getList())
    sll.DeleteNodeAtGivenPosition(10)
    print(sll.getList())
