'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1:
            return ''.join(sorted(s))     # O(nlogn)
        
        n = len(s)
        if n == 1:
            return s
        m = s
        
        # ---O(n^2)----
        for i in range(n):         # O(n)
            s = s[1:] + s[0]
            m = min(m,s)         # O(n)
        return m
'''    
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))