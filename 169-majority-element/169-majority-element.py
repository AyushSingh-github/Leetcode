'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        
        d = (sorted(d.items() , key = lambda x: x[1] , reverse = True))
        #print(dict(d))
        return d[0][0] 
'''

class Solution:
    def majorityElement(self, A: List[int]) -> int:
        N = len(A)
        count = 0
        element = 0
        
        #  identifing the majority element
        for i in A:
            if count == 0:
                element = i
                
            if i == element:
                count += 1
            else:
                count -= 1
        #  confirming that the element is majority or not      
        count = 0
        for i in A:
            if element == i:
                count += 1
            if count > N // 2:
                return element
        
        return -1