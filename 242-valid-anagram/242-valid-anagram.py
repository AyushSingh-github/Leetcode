class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t) or len(s) < len(t):
            return False
        
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        #print(s,t)
        
        for i,j in zip(s,t):
            if i!=j:
                return False
        return True
            
            
        