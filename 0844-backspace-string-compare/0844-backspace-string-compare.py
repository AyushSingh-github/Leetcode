#TC-> O(m+n),   SC-> O(m+n)

class Solution:
    '''
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
     '''  

#TC-> O(m+n),   SC-> O(1)    
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        index = 0
        while index < len(s):
            if s[index] == "#" and index != 0:
                s = s[:index-1] + s[index+1:]
                index -= 1
                continue
            
            index += 1
        
        index = 0
        while index < len(t):
            if t[index] == "#" and index != 0:
                t = t[:index-1] + t[index+1:]
                index -= 1
                continue
            
            index += 1
        
        s = s.replace("#","")
        t = t.replace("#","")
        
        return s == t
        