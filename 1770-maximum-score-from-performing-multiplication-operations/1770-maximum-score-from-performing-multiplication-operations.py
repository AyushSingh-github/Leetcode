class Solution:
	def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

		score = [0]
		mn = -1000*1000*1000
		for rd, multiplier in enumerate(multipliers,1):

			l1 =  [score[i]+num*multiplier for i,num in enumerate(nums[rd-1::-1])] +[mn]
			l2 =  [mn]+[score[i] + num * multiplier for i, num in enumerate(nums[:-(rd+1):-1])]
			score = [max(l1[i],l2[i])for i in range(rd+1)]

		return max(score)