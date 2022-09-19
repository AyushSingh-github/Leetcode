'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #brute force. TC = O(N+N)   SC = O(1)

        count0,count1,count2 =0,0,0
        for i in nums:
            if i==0:
                count0+=1
            elif i==1:
                count1+=1
            else:
                count2+=1
                
        for i in range(count0):
            nums[i]=0
        for i in range(count0,+count0+count1):
            nums[i]=1
        for i in range(count0+count1, count0+count1+count2):
            nums[i]=2
        return nums
'''
#Most optimized solution using Dutch National Flag Algorithm
#   3 way partitioning      TC = O(N),  SC = O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        mid, low = 0,0
        high = len(nums)-1
        
        while mid <= high:    
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low +=1
            elif nums[mid] == 2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -=1
                mid-=1

            mid+=1