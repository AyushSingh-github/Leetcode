class Solution:
    def integerReplacement(self, n: int) -> int:
        '''
        count = 0
        while n != 1:
            if n%2 == 0:
                n /= 2
            elif (n%4 == 1 or n == 3):
                n -= 1
            else:
                n += 1
            count += 1
        return count
        '''
        
        def fun(n,count):
            if n==1:
                return count
            if n%2==0:
                return fun(n/2,count+1)
            else:
                return min(fun(n+1,count+1),fun(n-1,count+1))
        
        return fun(n,0)