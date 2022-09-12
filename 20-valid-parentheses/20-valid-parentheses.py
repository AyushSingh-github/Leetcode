class Solution:
    def isValid(self, s: str) -> bool:
        '''
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
        '''
        '''
        st = []
        set = ('()','[]','{}') 
        
        for i in s:
            if (i == '(' or i == '{' or i == '['):
                st.append(i)
            elif (len(st)!=0 and (st[-1] + i) in set):
                st.pop()
            else:
                return False
            
        return True if len(st)==0 else False
        '''
        st = []
        d = { ")":"(" , "]":"[" , "}":"{" }
        
        if(len(s)==1):
            return False
        
        for i in s:
            if i in ["(","[","{"]:
                st.append(i)
            else:
                if (st and st[-1]==d[i]):
                    st.pop()
                else:
                    return False
        
        return True if len(st)==0 else False
                
                
