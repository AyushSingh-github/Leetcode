#wrong ans recursion
'''
class Solution:
    #lru_cache(2000)
    def fun(self,v,index,n):
        if n==0:
            return 0
        if (n<0 or index<0):
            return 10007
        
        left = 1 + self.fun(v,index,n-v[index])
        right = self.fun(v,index-1,n)
        return min(left,right)
        
    def numSquares(self, n: int) -> int:
        v = []
        k = 1
        
        for i in range(1,n+1):
            v.append(i)
            i += 2*k+1
            k+=1
        
        index = len(v)-1
        return self.fun(v,index,n)
'''

#recursion
'''
class Solution:
    def __init__(self):
        self.hash = dict()
        
    def numSquares(self, n: int) -> int:
        
        if n in self.hash:
            return self.hash[n]
        
        if int(math.sqrt(n))**2 == n:
            self.hash[n] = 1
            return 1
        
        minComb = float('inf')
        for i in range(1, n // 2 + 1):
            minComb = min(minComb, self.numSquares(i) + self.numSquares(n - i))
        self.hash[n] = minComb
        return minComb
'''    
    
#DP Approach
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [i**2 for i in range(0, int(sqrt(n)) + 1)]
        numsSet = set(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if i in numsSet:
                dp[i] = 1
                continue
            for num in nums:
                if num >= i:
                    break
                dp[i] = min(dp[i], dp[i - num] + 1)
        
        return dp[-1]
'''       

#Greedy DFS Approach
'''
class Solution:
    def numSquares(self, n: int) -> int:
        
        squareNums = [i**2 for i in range(1, int(sqrt(n)) + 1)]
        squareNumsSet = set(squareNums)
        def isDiv(n, count):
            if count == 1:
                return n in squareNumsSet
            if n < 0:
                return False
            for i in squareNums:
                if isDiv(n - i, count - 1):
                    return True
            return False
        
        for i in range(1, n + 1):
            if isDiv(n, i):
                return i
        return -1
'''            

#Greedy BFS Approach

class Solution:
    def numSquares(self, n: int) -> int:
        
        numsSquared = set([i**2 for i in range(1, int(sqrt(n)) + 1)])
        
        q = set([n])
        ans = 0
        while q:
            ans += 1
            newQ = set()
            for i in q:
                if i in numsSquared:
                    return ans
                for n2 in numsSquared:
                    if n2 < i:
                        newQ.add(i - n2)
            q = newQ
