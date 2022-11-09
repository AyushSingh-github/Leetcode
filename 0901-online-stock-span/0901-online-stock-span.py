#monotonic stack
'''
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        
        self.stack.append([price, ans])
        return ans
'''
class StockSpanner:
    def __init__(self):
        self.monostack = [(1e10, -1)]
        self.index = -1
    
    def next(self, price: int) -> int:
        self.index += 1
        # if self.monostack[-1][0] > price:
        #     self.monostack.append([price, self.index])
        #     return 1
    
        while self.monostack[-1][0] <= price:
            self.monostack.pop()
    
        self.monostack.append([price, self.index])
        return self.index - self.monostack[-2][1]
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
