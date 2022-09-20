class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        def compare_offset(n1, n2, offset):
            longest = 0
            same_counter = 0
            for i in range(offset, len(n1)):
                if (i-offset) > len(n2) -1:
                    break
                    
                if n1[i] == n2[i-offset]:
                    same_counter += 1
                else:
                    same_counter = 0
                longest = max(longest, same_counter)
            return longest
        
        
        best = 0
        # slide one way
        for i in range(len(nums1)):
            length = compare_offset(nums1, nums2, i)
            best = max(best, length)

        # then slide the next
        for i in range(len(nums2)):
            length = compare_offset(nums2, nums1, i)
            best = max(best, length)

        return best