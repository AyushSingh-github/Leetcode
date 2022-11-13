class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for item in nums:
            if item != val:
                nums[index] = item
                index +=1
        return index
        