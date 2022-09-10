class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        if k==0: return 0
        dp = [[1000, 0] for _ in range(101)]
        for price in prices:
            for i in range(1, k + 1):
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                dp[i][1] = max(dp[i][1], price - dp[i][0])
        return dp[k][1]
        '''
        #Neetcode
        @cache
        def dfs(i, buying, leftitem):
            if not leftitem or i >= len(prices): return 0
            
            m = dfs(i + 1, buying, leftitem)
            if buying:
                m = max(m, dfs(i + 1, not buying, leftitem) - prices[i])
            else: 
                m = max(m, dfs(i + 1, not buying, leftitem - 1) + prices[i])
            return m
        
        ans = dfs(0, True, k)
        
        return ans