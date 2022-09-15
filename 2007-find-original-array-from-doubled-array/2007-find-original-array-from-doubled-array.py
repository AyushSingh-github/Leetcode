'''
class Solution:
    def findOriginalArray(self, nums: List[int]) -> List[int]:
            ans = []
            if len(nums)%2:
                return ans
            nums.sort()
			
            d = {}
            for i in nums:
                d[i] = d.get(i,0)+1
                
            for i in nums:    
                if d[i] == 0:
                    continue
                elif d.get(2*i,0) >= 1:
                    ans.append(i)
                    d[2*i] -= 1
                    d[i] -= 1
                else:        
                    return []
                
            return ans
'''
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        # use Counter to count the frequency of each element in `changed`
        cnt, ans = Counter(changed), []
        
        # if the length of the input is odd, then return []
        # because doubled array must have even length
        if len(changed) % 2: return []
        
        # sort in ascending order
        for x in sorted(cnt.keys()):
            
            # if the number of cnt[x] is greater than than cnt[x * 2]
            # then there would be some cnt[x] left
            # therefore, return [] here as changed is not a doubled array
            if cnt[x] > cnt[x * 2]: return []
        
            # handle cases like [0,0,0,0]
            if x == 0:
                
                # similarly, odd length -> return []
                if cnt[x] % 2:
                    return []
                else: 
                    
                    # add `0` `cnt[x] // 2` times 
                    ans += [0] * (cnt[x] // 2)
            else:
                
                # otherwise, we put the element `x` `cnt[x]` times to ans
                ans += [x] * cnt[x]
            cnt[2 * x] -= cnt[x]
        return ans