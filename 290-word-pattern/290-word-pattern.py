class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        mp1 = defaultdict(list)
        mp2 = defaultdict(list)

        for i, value in enumerate(pattern):
            mp1[value].append(i)
        print(mp1)
             
        for i, value in enumerate(s):
            mp2[value].append(i)
        print(mp2)
            
        for k, v in zip(mp1.values(), mp2.values()):
            print(k,v)
            if k != v:
                return False 
        
        return len(mp1) == len(mp2)