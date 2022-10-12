class Solution:
    #O(N2)
    '''
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        for i in range(n-1):
            for j in range(i+1,n):
                if prices[i]>=prices[j]:
                    prices[i]-=prices[j]
                    break
    
        return prices
        '''
        
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            
            # comparing the previous element with current element as descibed in the question to calculate the discount.
            while stack and (prices[stack[-1]] >= prices[i]):
                
                # reducing the price of the current elem from previous.
                prices[stack.pop()] -= prices[i]
                
            #In stack we`ll just stores the index of the prices. Using those indexes will make changes in the prices list itself.
            stack.append(i) 
            
        return prices 