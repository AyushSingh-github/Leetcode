class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #O(N2)
        '''
        if len(s) < 10:
            return 
        ans = set()
        for i in range(len(s)-10):
            if s[i:i+10] in s[i+1:]:
                ans.add(s[i:i+10])
                
        return ans
        '''
        
        dic = {} 
        start = 0
        last = 9
        while last < len(s):
            if s[start:last+1] in dic:
                dic[s[start:last+1]] += 1
            else:
                dic[s[start:last+1]] = 1
            start += 1
            last += 1
        res = []
        for key in dic:
            if dic[key] > 1:
                res.append(key)
        return res