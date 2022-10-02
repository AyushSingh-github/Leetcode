class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        #TLE    no memo
        '''
        if(n > target or target > n*k):
            return 0 
        if(n==0 and target!=0):
            return 0 
        if(n==0 and target==0):
            return 1
        
        count=0
        for i in range(1,k+1):
            temp = self.numRollsToTarget(n-1, k, target-i)
            if(temp!=0):
                count += temp
        return count % (10**9 + 7)
        '''
        
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9+7

        @lru_cache(3000)
        def helper(n, target):
            if target < n or target > n*k:
                return 0 
            if n == 1:
                return 1
            
            s = 0 
            for i in range(1, k+1): 
                s += helper(n-1, target-i) 
            return s
            
        return helper(n, target) % mod