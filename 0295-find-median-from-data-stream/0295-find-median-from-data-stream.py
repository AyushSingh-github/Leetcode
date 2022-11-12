#sorting
'''
class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        # We're maintaining a monotone increasing list by inserting element using binary search
        bisect.insort(self.data, num)

    def findMedian(self) -> float:
        n = len(self.data)
        return self.data[n//2] if n&1 else (self.data[n//2] + self.data[n//2-1]) / 2
'''

#heap
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
        
    def addNum(self, num: int) -> None:
        # first offer to max heap
        heappush(self.maxHeap, -num)
        # bring highest of maxheap to min heap
        heappush(self.minHeap, -heappop(self.maxHeap))
        
        # if heaps become unbalanced
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
            

    def findMedian(self) -> float:
        # if stream is odd
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        # else mean of mids
        return (-self.maxHeap[0] + self.minHeap[0]) * 0.5
    
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()