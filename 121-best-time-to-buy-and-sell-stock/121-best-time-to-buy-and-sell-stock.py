class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stocks = len(prices) - 1

        max_left = prices[-1]
        profit = 0
        while stocks>=0:
            if max_left < prices[stocks]:
                max_left = prices[stocks]
            
            if max_left > prices[stocks]:
                profit = max(profit,max_left - prices[stocks])
            stocks-=1

        return profit 