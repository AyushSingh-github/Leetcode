#TC-> O(m+n),   SC-> O(m+n)
#stack
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
#slicing    
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

    
'''    Just use a helper function to move the two comparing potiners.
But the starting positions of the two pointers are tricky.
We start from the out-of-bound position from the end, and this simple trick can make the code concise.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValid(string: str, i: int) -> int:
            """
            Given the index i, and the string, output the next valid position at the left.
            When next valid position out of bound, return -1.
            """
            backspace = 0
            while backspace >= 0:
                i -= 1
                if i < 0: return -1
                if string[i] == "#": backspace += 1
                else: backspace -= 1
            return i
        
        p, q = len(s), len(t)  # two pointers starting from the end (which is out of bound)
        while p >= 0 and q >= 0:
            p, q = nextValid(s, p), nextValid(t, q)
            if p >= 0 and q >= 0 and s[p] != t[q]: return False
        return p * q > 0  # p < 0 and q < 0 
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        TWO POINTERS
        iterate through the string while maintaining a pointer for each 
        string
        
		while iterating through the string:
		- if the character is # and pointer is greater than 0: decrement pointer by 1
		- if the characte is # but pointe is 0, continue
		- if the character is anything other than #, replace the pointer'th index in string by that character and increment pointer by 1
        """
        p1 = 0
        p2 = 0
        s = list(s)
        t = list(t)
        
        for i in range(len(s)):
            if s[i] == '#':
                if p1 > 0:
                    p1 -= 1
            else:
                s[p1] = s[i]
                p1 += 1
            
        for i in range(len(t)):
            if t[i] == '#':
                if p2 > 0:
                    p2 -= 1
            else:
                t[p2] = t[i]
                p2 += 1
        
        s = s[:p1]
        t = t[:p2]
        
        return s == t