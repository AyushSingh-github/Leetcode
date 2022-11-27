'''
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # can generate all possible sequences and then at every origin point and the check if it is a arithematic slice
        n = len(A)
        def bt_aslices(index, path, size):
            
            if (index, tuple(path), size) in memo: return memo[(index, tuple(path), size)]
            if len(path) == size:
                for i in range(2, len(path)):
                    if abs(path[i] - path[i - 1]) != abs(path[i - 1] - path[i - 2]): return 0

                return 1
                    
            slices = 0
            for start in range(index, n):
                if start < n:
                    path.append(A[start])
                    slices += bt_aslices(start + 1, path, size)
                    path.pop()
            
            memo[(index, tuple(path), size)] = slices
            return slices
        
        res = 0
        A.sort()
        for size in range(3, n + 1):
            memo = dict()
            res += bt_aslices(0, [], size)        
        
        return res
'''
'''
class Solution:
    def __init__(self):
        self.out = 0
    
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dfs(dep,nums, cur):
            if dep == n:
                if len(cur) < 3:
                    return 
                diff = cur[1] - cur[0]
                for i in range(1, len(cur)):
                    if cur[i]- cur[i-1] != diff:
                        return
                self.out+=1
                return
            dfs(dep+1, nums, cur)
            cur.append(nums[dep])
            dfs(dep+1, nums, cur)
            cur.remove(nums[dep])
            
        cur = []
        dfs(0,nums, cur)
        return self.out
'''

class Solution:
	def numberOfArithmeticSlices(self, nums: List[int]) -> int:
		d = [defaultdict(int) for _ in range(len(nums))]
		ans=0
		for i in range(1,len(nums)):
			for j in range(i):
				cd = nums[i]-nums[j]
				jj = d[j][cd]
				ii = d[i][cd]
				ans+=jj
				d[i][cd]=jj+ii+1
		return ans
