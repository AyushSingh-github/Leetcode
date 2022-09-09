class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t) or len(s) < len(t):
            return False
        
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        #print(s,t)
        

        flag = 1
        for i,j in zip(s,t):
            if i!=j:
                flag = 0
        
        return True if flag else False
            
            
        