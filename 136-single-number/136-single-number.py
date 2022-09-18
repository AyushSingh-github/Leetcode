class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        #print(d)
        d = (sorted(d.items(), key = lambda x:x[1]))
        #print(d[0][0])
        return d[0][0]