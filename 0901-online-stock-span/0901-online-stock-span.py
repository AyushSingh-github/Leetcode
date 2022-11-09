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

#a different trick for dealing with the corner cases: add 1 pair in the initial stack. the ans = 1 and add up in the standard solution may be a little bit hard to understand.
class StockSpanner:
    '''
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
    '''
    def __init__(self):
        self.ledger = [-1]
        self.jump = dict()
        
    def next(self, price: int) -> int:
        # add price to ledger and add entry for jump
        self.ledger.append(price)
        p_idx = len(self.ledger)-1
        if p_idx == 1:
            return 1 # first entry
        
        # check previous val
        prev = self.ledger[p_idx-1]
        prev_idx = p_idx-1
        
        if prev <= price:
            while prev <= price and prev_idx > 0:
                if prev_idx in self.jump:
                    prev_idx = self.jump[prev_idx]
                else:
                    prev_idx -= 1
                prev = self.ledger[prev_idx]
            self.jump[p_idx] = prev_idx+1
            return p_idx-prev_idx
        else:
            return 1
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
