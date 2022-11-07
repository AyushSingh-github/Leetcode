class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        
        if s[0] == '6':
            return str(9)+s[1:]

        for i in range(len(s)):
            if s[i] == '6':
                return s[:i]+str(9)+s[i+1:]
                break
        
        return s