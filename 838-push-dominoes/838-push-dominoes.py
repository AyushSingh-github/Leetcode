class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #O(N2)
        '''
        temp = str()
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')
            dominoes = dominoes.replace('R.', 'RR')
            dominoes = dominoes.replace('.L', 'LL')

        return  dominoes.replace('xxx', 'R.L')
        '''
        #O(N)   using Queue
        
        dom = list(dominoes)
        q = deque()
        
        for i,d in enumerate(dom):
            if d!='.':
                q.append((i,d))
                
        while q:
            i,d = q.popleft()
            
            if d == "L" and i>0 and dom[i-1] == ".":
                q.append((i-1,"L"))
                dom[i-1] = "L"
            elif d == "R":
                if i+1 < len(dom) and dom[i+1] == ".":
                    if i+2 < len(dom) and dom[i+2] == "L":
                        q.popleft()
                    else:
                        q.append((i+1,"R"))
                        dom[i+1] = "R"
                        
        return str("".join(dom))