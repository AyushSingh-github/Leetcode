class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #d=Counter(nums)
        #print(d)
        '''
        for i in range(len(d)):
        accessing dic element by index without function- convert into list then indexing works
            #print(list(d)[i])
            #res=(target-list(d)[i])
        '''
        d={}
        for index, num in enumerate(nums):
            if target-num in d:
                return [d[target-num], index]
            d[num] = index
                
            