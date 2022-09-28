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
        i = 0
        j = 9
        while j < len(s):
            if s[i:j+1] in dic:
                dic[s[i:j+1]] += 1
            else:
                dic[s[i:j+1]] = 1
            i += 1
            j += 1
        res = []
        for k in dic:
            if dic[k] > 1:
                res.append(k)
        return res        