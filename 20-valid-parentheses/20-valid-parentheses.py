class Solution:
    def isValid(self, s: str) -> bool:
        start = True
        while start:
            if '{}' in s:
                s = s.replace('{}','')
            elif '()' in s:
                s = s.replace('()','')
            elif '[]' in s:
                s = s.replace('[]','')
            else:
                start = False
                
        return True if len(s)==0 else False
