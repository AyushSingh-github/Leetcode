class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        #for loop
        '''
        n = len(s)
        integer = 0 # running sum
        last_value = 0 # keep track of last value
        
        # Iterate backwards
        for i in range(1,n+1):
            value = romans[s[-i]]
            
            # when the new value is larger or equal to previous, just add to sum
            if value >= last_value:
                integer += value
            
            # Else you must subtract the value from the sum
            else:
                integer -= value
            
            # update the last value seen
            last_value = value
        return integer
        '''
        
        #while loop
        total = 0
        i = 0
        while i < len(s):
            if i+1<len(s) and romans[s[i]] < romans[s[i+1]]:
                total+=romans[s[i+1]]-romans[s[i]]
                i+=1
            else:
                total+=romans[s[i]]
            i+=1
        return total