```
# * Iterative Bottom-Up Solution | O(mn) Time | O(mn) Space
# * m -> The length of nums1 array | n -> The length of nums2 array
​
​
class Solution:
def findLength(self, nums1: List[int], nums2: List[int]) -> int:
nums1_len, nums2_len = len(nums1), len(nums2)
# * Create a 2-D DP with the rows as nums1_len + 1 (Including empty subarray)
# * and cols as nums2_len + 1 (Including empty subarray).
dp = [[0 for _ in range(nums2_len + 1)] for _ in range(nums1_len + 1)]
​
max_subarray_len = 0
# * Start the iteration from the first row and first col.
for i in range(1, nums1_len + 1):
for j in range(1, nums2_len + 1):
# * If both elements match then we set the value by chopping
# * the current element in both the arrays and adding 1 to it.
if nums1[i - 1] == nums2[j - 1]:
dp[i][j] = 1 + dp[i - 1][j - 1]
max_subarray_len = max(max_subarray_len, dp[i][j])
​
return max_subarray_len
```