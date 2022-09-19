class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # HashMap solution. TC = O(N^2.log(n))    SC = [O(N) + O(M)] -> hash + set space
        '''
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
        '''
        
        #two pointer (D&C) changing the question as two sum using 
        # TC = O(N^2)  SC = O(M) auxilary space so equals O(1)
        
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                lo = i+1
                hi = len(nums)-1
                a = -(nums[i])
                
                while lo<hi:
                    if nums[lo] + nums[hi] == a:
                        res.append([nums[i],nums[lo],nums[hi]])
                        
                        while lo<hi and nums[lo]==nums[lo+1]:
                            lo+=1
                        while lo<hi and nums[hi]==nums[hi-1]:
                            hi-=1
                        lo+=1
                        hi-=1
                        
                    elif (nums[lo]+ nums[hi]<a):
                        lo+=1
                    else:
                        hi-=1
        return res
                
            
            
            
            
            