#TLE but works    (sorting + two pointer on maximum and minimum)
'''
class Solution:
    def threeSumClosest(self, a: List[int], x: int) -> int:
        def find(i,j,k):
            if i>=j:
                return 
            s=a[i]+a[j]+a[k]
            if s>=t[0]:
                find(i,j-1,k)
            elif s<t[1]:
                find(i+1,j,k)
            else:
                t[0]=x+abs(s-x)
                t[1]=x-abs(s-x)
                res[0]=s
                find(i+1,j,k)
                find(i,j-1,k)
                
        
        n=len(a)
        a.sort()
        res=[0]
        t=[math.inf,-math.inf]
        for k in range(n-2):
            i=k+1
            j=n-1
            find(i,j,k)
        return res[0]
'''
#O(N2) =  two pointer + sorting 
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        min_diff = 1e5
        ans = 1e5
        
        for i in range(0 , len(nums) - 2):   
            if i == 0 or nums[i] != nums[i-1]:
                low = i + 1
                high = len(nums) - 1
                while low < high:
                    temp = nums[i] + nums[low] + nums[high]
                    if abs(target - temp) < min_diff:
                        min_diff = abs(target - temp)
                        ans = temp
                    if temp == target:
                        return target
                    elif temp < target:
                        low += 1
                    else:
                        high -= 1
        return ans
'''
import sys
class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		n = len(nums)
		ans = 0
		diff = sys.maxsize

		for i in range(n):
			l , r = i + 1, n - 1

			while l < r:
				currSum = nums[i] + nums[l] + nums[r]

				if currSum == target:
					return currSum

				if currSum > target:
					r -= 1
				else:
					l += 1

				if abs(target - currSum) < diff:
					ans = currSum
					diff = abs(target - currSum)
		return ans