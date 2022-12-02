'''
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1=Counter(word1)
        d2=Counter(word2)
        t1, t2= [],[]
        
        if len(word1)!=len(word2) and len(d1)!=len(d2): 
            return 0
        for ele in d2:
            if ele in d1 and d1[ele]==d2[ele]:
                pass
            elif ele in d1:
                t1.append(d1[ele])
                t2.append(d2[ele])
            else:
                return 0
            
        if len(t1)!=len(t2):
            return 0
        t1.sort()
        t2.sort()
        
        if t1!=t2:
            return 0
        return 1
    
'''

   
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        flag1,flag2 = 0,0
        if set(word1) == set(word2):
            flag1 = 1
        
        if sorted(Counter(word1).values())==sorted(Counter(word2).values()):
            flag2 = 1
            
        if (flag1 and flag2) == 1:
            return True

        ##  QUERY 1:::to check whether elements of word1 and word 2 ,where set() function helps to remove the repeated numbers

        ##  QUERY 2::to check the occurance of the  digit od the word1 and word2 we use COUNTER(),inbulit function to countent the occurance of the digits in word 1 and word 2 ,
        ##the sort the by using the SORTED(),function to check whether the word1 and word 2 are equal by transform of any occurance