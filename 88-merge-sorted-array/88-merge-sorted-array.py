class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        nums2_list = 0
        stack = []
        
        for i in range(m+n):
            if i<m:
                stack.append(nums1[i])
                 
            if stack and nums2_list < n :
                if stack[0] < nums2[nums2_list]:
                    nums1[i] = stack.pop(0)
                else:
                    nums1[i] = nums2[nums2_list]
                    nums2_list += 1
            elif stack:
                nums1[i] = stack.pop(0)
            else:
                nums1[i] = nums2[nums2_list]
                nums2_list += 1