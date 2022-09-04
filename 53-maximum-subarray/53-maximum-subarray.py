class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev=-99999
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            if(prev<summ):    
                prev=summ
            if(summ<0):
                summ=0
        return prev