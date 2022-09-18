class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        d = Counter(nums)
        #print(d)
        d = (sorted(d.items(), key = lambda x:x[1]))
        #print(d[0][0])
        return d[0][0]
        '''
        
        d = {}
        for i in nums:
            d[i] = d.get(i,0) +1
        #print(d)
        
        for i in d:
            if d[i] == 1:
                return i