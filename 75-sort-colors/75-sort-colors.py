class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
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

    def sortColors(self, nums: List[int]) -> None:
        
        mid = low = 0
        high = len(nums)-1
        
        def swap(a,b):
            temp = nums[a]
            nums[a]= nums[b]
            nums[b] = temp
        
        while mid <= high:
            
            if nums[mid] == 0:
                swap(low,mid)
                low +=1
            elif nums[mid] == 2:
                swap(mid,high)
                high -=1
                mid-=1
            
            mid+=1
'''