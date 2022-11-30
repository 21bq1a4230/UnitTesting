class Stack:
    def __init__(self):
        """your code here"""
        self.t = 0
        self.lt = []
        self.top = -1

    def push(self, data):
        """your code here"""
        self.top += 1
        self.lt.insert(self.top, data)

    def pop(self):
        """your code here"""
        self.t = self.top
        self.top = self.top -1
        return self.lt.pop(self.t)

    def peek(self):
        """your code here"""
        if self.top == -1:
            return None
        return self.lt[self.top]


if __name__ == "__main__":
    stk = Stack()
    stk.push(4)
    stk.push(3)
    stk.push(2)
    print(stk.peek())
