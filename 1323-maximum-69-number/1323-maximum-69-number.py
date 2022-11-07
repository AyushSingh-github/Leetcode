class Solution:
    def maximum69Number (self, num: int) -> int:
        #using string:      TC-> O(N)
        '''
        s = str(num)
        if s[0] == '6':
            return str(9)+s[1:]

        for i in range(len(s)):
            if s[i] == '6':
                return s[:i]+str(9)+s[i+1:]
                break
        return s
        '''
        
        #using maths
        curr_index,indexsix,copy = 0,-1,num
        
        while copy:
            if copy%10 == 6:
                indexsix = curr_index
            
            copy //= 10
            curr_index += 1
            
        return  num if indexsix == -1 else num + 3*10**indexsix   # [9669 + 3*10*2 (300)] = 9969