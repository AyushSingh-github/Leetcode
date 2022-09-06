class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def solve(largelist, d):
            res = []
            for i in largelist:
                if i in d and d[i] > 0:
                    res.append(i)
                    d[i] -= 1
            return res

        if len(nums1) < len(nums2):
            d = collections.Counter(nums2)
            return solve(nums1, d)
        else:
            d = collections.Counter(nums1)
            return solve(nums2, d)
        