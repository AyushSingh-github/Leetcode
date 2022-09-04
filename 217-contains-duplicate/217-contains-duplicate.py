class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            print(i)
            if nums[i]==nums[i+1]:
                return True
            else:
                False
                
                
                