'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # HashMap solution. TC = O(N^2.log(n))    SC = [O(N) + O(M)] -> hash + set space
        
        d={}
        s = set()
        res = []
        for i in nums:
            d[i] = d.get(i,0)+1
        #print(d)
        
        #checking the (nums[i] + nums[j]) == -c in d
        # if present then nums[i] + nums[j] + [c  or -(nums[i]+nums[j])] == 0 as {i+j = -k}
        
        for i in range(len(nums)):
            #decr value of ith ele in d as already used once now so only will need when this triplet is complete after the iteration and search in hashmap
            d[nums[i]]-=1
            
            for j in range(i+1,len(nums)-1):
                #same with jth ele in hashmap 
                d[nums[j]]-=1
                c = -(nums[i]+nums[j])
                if c in d and d[c]>=1: #only if the 3rd ele is present in hashmap and atleast once
                    k = [nums[i] , nums[j] , c]
                    k.sort()
                    t = tuple(k)  
                    
                    #adding in set for triplets found and only unique keys 
                    if t not in s:
                        s.add(t)
                # incr original freq in hashmap as we might need the same with other unique triplet in future 
                d[nums[j]]+=1
            d[nums[i]]+=1
        for i in s:
            res.append(list(i))
        return res
        
        
        #two pointer (D&C) changing the question as two sum using 
        # TC = O(N^2)  SC = O(M) auxilary space so equals O(1)
        #Striver Concept
        
        nums.sort()
        res = []
        
        #example list = [-2,-2,-1,-1,-1,0,0,0,2,2,2]
        
        # 'i' is 'a' here and we take 'a' as constant and move only to distinct nums from [-2 -> -1 -> 0 -> 2] as the summ remain in (b+c = -a) eqn
        
        for i in range(len(nums)-2):  # only till last 3rd num as 'a' must have 2 nums lo and hi which make the triplet 
            
            #i or 'a' is the remain in eqn that we check when its in start or further away and dont repeat the same value as previous 'a'
            
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                lo = i+1            #lo is 'b'
                hi = len(nums)-1    #hi is 'c'  in eqn  b+c = -a
                a = -(nums[i])      #neg of a to simplify
                
                while lo<hi:
                    if nums[lo] + nums[hi] == a:
                        #triplet found
                        res.append([nums[i],nums[lo],nums[hi]])
                        
                        #incr lo and hi to its new pos and should not be same as before lo and hi value
                        while lo<hi and nums[lo]==nums[lo+1]:
                            lo+=1
                        while lo<hi and nums[hi]==nums[hi-1]:
                            hi-=1
                        #final and diff pos from the last values 
                        lo+=1
                        hi-=1
                        
                    # if sum of b+c < a,  that mean we need to incr the sum towards the 'a' by incr lo value towards the larger side else decr the curr sum to get value closer to 'a' by incr hi
                    elif (nums[lo]+ nums[hi]<a):
                        lo+=1
                    else:
                        hi-=1
        return res
                
'''            
            
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    arr.append((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return set(arr)               
            