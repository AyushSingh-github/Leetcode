class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[1000, 0] for _ in range(101)]
        for price in prices:
            for i in range(1, k + 1):
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                dp[i][1] = max(dp[i][1], price - dp[i][0])
        return dp[k][1]