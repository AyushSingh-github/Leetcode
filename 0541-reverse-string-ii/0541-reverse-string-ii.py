class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<=k:
            return s[::-1]
        l = list(s)
        
        for i in range(0,len(s),2*k):
            l[i:i+k] = reversed(l[i:i+k])
            
        return "".join(l)