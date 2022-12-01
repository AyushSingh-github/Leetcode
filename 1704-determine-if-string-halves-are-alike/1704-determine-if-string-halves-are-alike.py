class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        c1,c2 =0,0
        for i in a:
            if i in vowel:
                c1 += 1
                
        for i in b:
            if i in vowel:
                c2 += 1
                
        if c1==c2:
            return True
        return False