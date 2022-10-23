class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup,missing = -1,1
        for i in range(1,len(nums)):
            if (nums[i]==nums[i-1]):
                dup = nums[i]
            elif (nums[i] > nums[i-1]+1):
                missing = nums[i - 1] + 1
                
        if nums[len(nums)-1] != len(nums):
            return [dup,len(nums)]
        
        return [dup,missing]
