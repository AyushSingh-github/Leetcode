#@chuilinux/StefanPochmann's 1-liner 
#   return num > 0 == 30**32 % num
#   where a > b == c means a > b and b == c

# 30^32 = (2^32)*(3^32)*(5^32) will also work for py.

#   q = (2^30)*(3^20)*(5^13) = 4570198050078720000000000000

# what's 2^30, 3^20, and 5^13???
# These are the max 2/3/5^x number < 2^31-1

'''
The math trick is:
if x = 2^i then 2^30 % x == 0
AND if y = 3^j then 3^20 % y == 0
AND if z = 5^k then 5^13 % z == 0
where n = 2^i * 3^j * 5^k

For example:
n = 2^1 * 3^2 * 5^3 = 2250
a%x * b%y * c%z = (2^30) % 2^1 * (3^20) % 3^2 * (5^13) % 5^3 = 0
'''

#brute force - 
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1: 
            return False
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else: return False
        return True