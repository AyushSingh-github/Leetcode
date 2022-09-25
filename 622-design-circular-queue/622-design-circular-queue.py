#linked list
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.counter = 0
        self.pointer = None

    def append(self, val):
        if self.head is None:
            self.head = ListNode(val)
            self.head.next = self.head
            self.pointer = self.head
        else:
            self.pointer.next = ListNode(val, self.head)
            self.pointer = self.pointer.next
        self.counter+=1
        return True
        
    def remove(self):
        if self.head is None:
            return False
        if self.counter == 1:
            self.head = None
            self.pointer = None
            self.counter-=1
            return True
        self.head = self.head.next
        self.pointer.next = self.head
        self.counter-=1
        return True
    
    def enQueue(self, value: int) -> bool:
        if self.counter < self.k:
            return self.append(value)
        return False
    
    
    def deQueue(self) -> bool:
        if self.counter > 0:
            return self.remove()
        return False
        
    def Front(self) -> int:
        if self.head is None:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.head is None:
            return -1
        return self.pointer.val

    def isEmpty(self) -> bool:
        return self.counter==0

    def isFull(self) -> bool:
        return self.counter==self.k
'''

#Arrays / Lists
class MyCircularQueue:
    
    def __init__(self, k: int):
        self.queue = []
        self.size = k
        
    def enQueue(self, value: int) -> bool:  
        if self.isFull(): 
            return False
        self.queue.append(value)
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.pop(0)
        return True
        
    def Front(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
        
    def Rear(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]
        
    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if len(self.queue) == self.size:
            return True
        return False

    
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()