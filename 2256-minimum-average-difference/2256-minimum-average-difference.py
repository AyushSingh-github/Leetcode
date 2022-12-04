#TC-> O(n2), SC-> O(1)
'''
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        min_avg_diff = math.inf
        
        for index in range(n):
            # Calculate average of left part of array, index 0 to i.
            
            left_part_average = 0
            for i in range(index + 1):
                left_part_average += nums[i]
                
            left_part_average //= (index + 1)
            
            # Calculate average of right part of array, index i+1 to n-1.
            right_part_average = 0
            
            for j in range(index + 1, n):
                right_part_average += nums[j]
        
            # If right part have 0 elements, then we don't divide by 0.
            if index != n - 1:
                right_part_average //= (n - index - 1)
            
            curr_difference = abs(left_part_average - right_part_average)
            
            # If current difference of averages is smaller,
            # then current index can be our answer.
            if curr_difference < min_avg_diff:
                min_avg_diff = curr_difference
                ans = index
                
        return ans
'''

#prefix-Sum
#TC-> O(N),     SC-> O(N)
'''
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        min_avg_diff = math.inf
        
        # Generate prefix and suffix sum arrays.
        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 1)
        
        for index in range(n):
            prefix_sum[index + 1] = prefix_sum[index] + nums[index];
        
        for index in range(n - 1, -1, -1):
            suffix_sum[index] = suffix_sum[index + 1] + nums[index];
        
        for index in range(n):
            
            # Calculate average of left part of array, index 0 to i.
            left_part_average = prefix_sum[index + 1]
            left_part_average //= (index + 1)
            
            # Calculate average of right part of array, index i+1 to n-1.
            right_part_average = suffix_sum[index + 1]
            
            # If right part have 0 elements, then we don't divide by 0.
            if index != n - 1:
                right_part_average //= (n - index - 1)
            
            curr_difference = abs(left_part_average - right_part_average)
            
            # If current difference of averages is smaller,
            # then current index can be our answer.
            if curr_difference < min_avg_diff:
                min_avg_diff = curr_difference
                ans = index
                
        return ans
'''

#Space Optmised

#My intuition led me to a slightly different variant of the Approach 3. Instead of storing the left sum and the total sum, I store the left sum and the right sum (which is equal the total sum initially).

'''
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        min_avg_diff = math.inf
        left_sum = 0
        right_sum = sum(nums) # right_sum instead of total_sum

        for index in range(n):
            left_sum += nums[index]
            right_sum -= nums[index] # A pure elegance
            
            left_part_average = floor(left_sum / (index + 1))
            right_part_average = floor(right_sum / (n - index - 1)) if index != n - 1 else 0
            
            curr_difference = abs(left_part_average - right_part_average)
            if curr_difference < min_avg_diff:
                min_avg_diff = curr_difference
                ans = index

                # A little shortcut because the difference can't be less than 0
                if curr_difference == 0:
                    break
                
        return ans

'''
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = 0
        total = sum(nums)
        ans= float(inf)
        index=0
        for i in range(len(nums)) :
            prefix += nums[i]
            l=i+1
            r=len(nums)-l
            suffix = total - prefix 
            ad = (prefix // l) - ((suffix//r) if r else 0)
            if abs(ad) < ans :
                ans=abs(ad)
                index=i 
        return index