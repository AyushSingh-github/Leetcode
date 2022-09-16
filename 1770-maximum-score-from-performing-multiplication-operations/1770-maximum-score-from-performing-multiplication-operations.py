class Solution:
	def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

		score = [0]
		mn = -1000*1000*1000
		for rd, multiplier in enumerate(multipliers,1):

			l1 =  [score[i]+num*multiplier for i,num in enumerate(nums[rd-1::-1])] +[mn]
			l2 =  [mn]+[score[i] + num * multiplier for i, num in enumerate(nums[:-(rd+1):-1])]
			score = [max(l1[i],l2[i])for i in range(rd+1)]

		return max(score)
'''
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n=len(nums)
        m=len(multipliers)
        
        #Recursion + Memoization - TLE
        
        dp=[[-1]*m for i in range(n)]
        def helper(low, high, j):
            if j==m:
                return 0

            if dp[low][j]!=None:
                return dp[low][j]

            first=nums[low]*multipliers[j]+helper(low+1, high, j+1)
            last=nums[high]*multipliers[j]+helper(low, high-1, j+1)
            dp[low][j]=max(first, last)
            return dp[low][j]
        
        return helper(0, n-1, 0)

        # Tablulation
        
        dp=[[0]*(m+1) for i in range(m+1)]
        for j in range(m-1, -1, -1):
            for low in range(j, -1, -1):
                first=nums[low]*multipliers[j]+dp[j+1][low+1]
                last=nums[n-1-(j-low)]*multipliers[j]+dp[j+1][low]
                dp[j][low]=max(first, last)
        return dp[0][0]
       ''' 