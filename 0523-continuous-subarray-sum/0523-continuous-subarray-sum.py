'''
Lets see an example to understand the approach
arr=[23,2,6,4,7],k=6
lets have a sum that adds the element in the sequence we parse them
first s=23 and s%k => 23%6 =5 and then we add 2 and than we add 6 and so
s=29 and s%k => 29%9 = 5 ,Now we know that we encountered remainder twice which tells us that we added number that is divisible by 6 which is true becuase after 23 we added 2+4=6
this the basic intuition behind the problem
Now we have to counter some cases we will have a hash map and store remainder in it to check if we already have encountered that after that we also store the index because we have to make sure that the subarrays added is atleat of length 2. To make sure the function doesnot return true if the first element is divisible by 6 we store inititialise hash_set as {0:0}
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # initialize the hash map with index 0 for sum 0
        track_remainder={0:-1}
        sums=0
        for i,a in enumerate(nums):
            #adding current elemnt to sums
            sums+=a
            #checking if not in sums%k in hash_set and and appending index if it is true
            if sums%k not in track_remainder:
                track_remainder[sums%k] = i
                
            #condition to check if the subarray is greater than equal to 2
            elif i-track_remainder[sums%k]>1:
                return True
        return False