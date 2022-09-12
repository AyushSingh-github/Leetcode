class MyQueue:
    def __init__(self):
        self.list = []
        self.index = 0 

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        t = self.list[self.index]
        self.index += 1
        return t

    def peek(self) -> int:
        return self.list[self.index]

    def empty(self) -> bool:
        if self.index == len(self.list):
            return True
        else:
            False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()