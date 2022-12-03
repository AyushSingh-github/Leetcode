class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        s = []
        
        for key,value in sorted(c.items(),key=lambda x:x[1],reverse = True):
            s.append(key*value)
            
        return str(''.join(s))
        
        '''
        ctr=collections.defaultdict(int)
        for i in s:
            ctr[i]+=1
        res=[]
        for k,v in sorted(ctr.items(),key=lambda x:x[1],reverse=True):
            res.append(k*v)
        return "".join(res)
        '''