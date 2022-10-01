class Solution:
    def numDecodings(self, s: str) -> int:
		# Initialize dp_a and dp_b
        dp1 = [0] * (len(s) + 1)
        dp2 = [0] * (len(s) + 1)
        
		# Get first value of dp_a
        if s[0] == '0':
            return 0
        else:
            dp1[1] = 1
        for i in range(1, len(s)):
            
            # Use dicussed technique to calculate in cases s[i] = '0'
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] =='2':
                    dp2[i+1] = dp1[i]
                else:
                    return 0
                
            else:
                # In all other cases construct a two-digit number and apply mentioned tactics
                digit = (ord(s[i-1])-48)*10 + ord(s[i])-48
                
                if digit <= 26:
                    dp2[i+1] = dp1[i]
                dp1[i+1] = dp1[i] + dp2[i]
                
            # Get last elements of both arrays and add tehm to get a final result
        return dp1[-1] + dp2[-1]