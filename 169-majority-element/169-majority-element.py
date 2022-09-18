class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        
        d = (sorted(d.items() , key = lambda x: x[1] , reverse = True))
        #print(dict(d))
        return d[0][0]