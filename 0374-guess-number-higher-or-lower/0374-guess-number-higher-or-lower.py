# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

#TC-> O(N)
'''
class Solution:
    def guessNumber(self, n: int) -> int:
        for i in range(1,n):
            if guess(i) == 0:
                return i
        return n
'''

class Solution:
    def guessNumber(self, n: int)-> int:
        low,high = 0,n+1
        while True:
            mid = (low+high)//2
            #print(mid)
            guessvalue = guess(mid)
            
            if guessvalue>0:
                low = mid
            elif guessvalue<0:
                high = mid
            else:
                return mid
            
            