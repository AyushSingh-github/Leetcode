class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        print(d)
        
        for index,val in enumerate(d):
            if d[val] ==1:
                if val in s:
                    return s.index(val)
        return -1
    
        '''
        for val in s:
            if s.count(val)==1:
                return s.index(val)
        return -1
        '''
        