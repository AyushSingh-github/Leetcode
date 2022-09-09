class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[i+1:] and  s[i] not in s[:i]:
                return i
        return -1

        '''
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        #print(d)
        
        for index,val in enumerate(d):
            if d[val] ==1 and val in s:
                return s.index(val)
        return -1
        '''
        '''
        for val in s:
            if s.count(val)==1:
                return s.index(val)
        return -1
        
        or -----------------------------------------------
        
		for i, j in Counter(s).items():
			if j == 1: return s.index(i)
		return -1        
        '''
        