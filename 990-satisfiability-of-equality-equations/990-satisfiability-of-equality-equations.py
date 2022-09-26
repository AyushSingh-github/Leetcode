class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = [i for i in range(26)]
        
        def find(e):
            #dfs type code to carry the parent for each value of the e in the string
            if (e!=parents[e]):
                parents[e] = find(parents[e])   #recursion
                #print(parents)
            return parents[e]
            
            
        for e in equations:
            if e[1] == "=":
            # union of first and last
                first = ord(e[0]) - 97
                last = ord(e[3]) - 97
                
            # make parent of first's value become the new parent of last value's parent
            # basically the first's parent be the parent of parent of last value
                parents[find(last)] = find(first)
                #print(parents[find(first)],parents[find(last)])
        
        for e in equations:
            if e[1] == "!":
                first = ord(e[0]) - 97
                last = ord(e[3]) - 97
                
                if find(first) == find(last):
                    return False
        
        return True
                 
                