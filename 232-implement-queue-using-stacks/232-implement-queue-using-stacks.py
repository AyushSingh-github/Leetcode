'''
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
'''

class MyQueue(object):
    
    def __init__(self):
        self.s1=deque()
        self.s2=deque()

    def push(self, x):
        if self.s1==False:
            self.s1.append(x)
        else:
            while self.s1:
                t=self.s1.pop()
                self.s2.appendleft(t)
            self.s1.append(x)

    def pop(self):
        if self.s2:
            return self.s2.pop()
        elif self.s1:
            return self.s1.pop()
        
    def peek(self):
        if self.s2:
            return self.s2[-1]
        else:
            return self.s1[-1]

    def empty(self):
        if self.s1 or self.s2:
            return False
        else:
            return True
                 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()