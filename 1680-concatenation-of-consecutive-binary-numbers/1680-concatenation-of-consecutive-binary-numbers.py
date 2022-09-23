class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # iteration- Learning purpose  TC = O(2N*logN)
        '''
        mod  = 1000000007
        bstr = ""
        for i in range(1,n+1):
            bstr += str(bin(i)[2:])
        #return int(bstr,2)%(pow(10,9)+7)
        return int(bstr,2)%mod
        '''
        #bit manipulation
        '''
        mod  = 1000000007
        ans = 1
        for i in range(2, n + 1):
            ans = (ans << i.bit_length()) % mod + i     
        return ans % mod
        '''
        constant = 10**9 + 7
        summation = 0
        bit_width = 0
        
        # iterate from 1 to n
        for i in range(1, n+1):
            
            # update binary bit width when we meet power of 2
            if i & i-1 == 0:
                bit_width += 1
            
            # use binary left rotation to implement concatenation
            summation = summation << bit_width
            
            # add with current number
            summation = summation | i
            
            # mod with constant defined by description
            summation %= constant
        
        return summation