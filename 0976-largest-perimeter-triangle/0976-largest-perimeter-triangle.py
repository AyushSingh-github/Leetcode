class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)-3, -1, -1):
            if nums[i+2] < nums[i] + nums[i+1]:
                return nums[i] + nums[i+1] + nums[i+2] 
        return 0