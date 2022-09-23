class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        #print(d)
        odd_ele = 0
        for i in d:
            if d[i]%2:
                odd_ele +=1
                d[i] -= 1
                
        ans = sum(d.values())
        #print(ans)
        
        if odd_ele:
            ans += 1
        return ans
        
