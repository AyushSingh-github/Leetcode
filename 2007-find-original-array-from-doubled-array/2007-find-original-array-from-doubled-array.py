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