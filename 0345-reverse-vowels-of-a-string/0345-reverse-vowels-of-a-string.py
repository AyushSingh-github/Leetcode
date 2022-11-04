class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        
        vowel =['a','e','i','o','u','A','E','I','O','U']
        i = 0
        j = len(s)-1
        
        while i<j:
            while s[i] not in vowel and i<j:
                i+=1
            while s[j] not in vowel and i<j:
                j-=1
            
            if s[i] in vowel and s[j] in vowel:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            
        return "".join(s)
            