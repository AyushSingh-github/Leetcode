'''
class Solution:
    def trap(self, height: List[int]) -> int:
        #stack max area histogram formula
        my_stack = []  # store the index
        total_volume = 0
        for i, v in enumerate(height):
            while my_stack and height[my_stack[-1]] <= v:
                h1 = height[my_stack.pop()]
                if my_stack:
                    h2 = min(height[my_stack[-1]], v)
                    total_volume += (h2 - h1) * (i - my_stack[-1] - 1)
            my_stack.append(i)
        return total_volume
'''

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        #left and right max height  (striver -> tc. O(n) and sc. O(n2))
        n = len(height)
        water = 0
        
        left = 0
        right = 0
        
        max_left = [0]*n
        max_right = [0]*n
        
        for i in range(n):
            if height[i] > left:
                left = height[i]
            max_left[i] = left
            
            #backwards
            j = n-1-i
            if height[j] > right: right = height[j]
            max_right[j] = right
        
        for i, h in enumerate(height):
            if max_left[i] > h and max_right[i] > h:
                water += min(max_left[i], max_right[i]) - h
                
        return water
'''   
#optimised

class Solution:
	def trap(self, height: List[int]) -> int:

		result = 0

		max_left = height[0]
		max_right = height[-1]

		l = 1
		r = len(height) - 2

		while l <= r:

			max_left = max(max_left, height[l])
			max_right = max(max_right, height[r])

			if max_left < max_right:
				result = result + max_left - height[l]
				l += 1
			else:
				result = result + max_right - height[r]
				r -= 1

		return result
