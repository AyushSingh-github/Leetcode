class Solution:
    def isPalindrome(self, x: int) -> bool:
        #pythonic
        #return str(x)[::-1] == str(x)
        
        #maths based
        num = x
        ans = 0
        if x < 0:
            return False
        while num!=0:
            ans = ans*10 +(num%10)
            num //= 10
        #print(ans)
        return ans == x
        