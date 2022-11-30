class Queue:
    def __init__(self):
        self.t = 0
        self.top = -1
        self.lt = []

    def Enqueue(self, data):
        self.top += 1
        self.lt.insert(0, data)

    def DeQueue(self):
        self.t = self.top
        self.top -= 1
        return self.lt.pop(self.t)

    def peekRear(self):
        return self.lt[0]

    def peekEnd(self):
        return self.lt[self.top]


if __name__ == "__main__":
    q = Queue()
    arr = ['a', 'e', 'i', 'o', 'u']
    for i in arr:
        q.Enqueue(i)

    print(q.peekRear())
