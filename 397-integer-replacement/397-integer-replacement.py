class Solution:
    def integerReplacement(self, n: int) -> int: 
        dp = {}
        def memo(n, dp):    
            if n == 1:
                return 0
        
            if n in dp:
                return dp[n]
            
            if n % 2 == 0:
                dp[n] = 1 + memo(n//2, dp)
                return dp[n]
            
            else:
                dp[n] = 1 + min(memo(n-1, dp), memo(n+1, dp))
                return dp[n]
            
        return memo(n, dp)