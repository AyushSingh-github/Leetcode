class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            lst = []
            for i in range(1, len(nums)):
                num = (nums[i] + nums[i-1]) % 10
                lst.append(num)
            nums = lst
        return sum(nums)