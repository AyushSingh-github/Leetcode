class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        max_count = 0
        # i from -4 to 4. so i+j value wil tell which ith and jth ele will overlap and
        #for each ith value we get diff jth value which in i+j < 0 that gives positive value of j,
        for i in range(-n+1,m):
            count = 0
            for j in range(n):
                if i+j<0:
                    continue
                elif i+j >=m:
                    break
                elif nums1[i+j] == nums2[j]:
                    count +=1
                    max_count = max(max_count,count)
                else:
                    count=0
        return max_count