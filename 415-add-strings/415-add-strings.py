class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        n = int(num1) + int(num2)
        return str(n)
        '''
        
        integer_1 = 0
        integer_2 = 0

        for i in num1:
            integer_1 = integer_1 * 10 + (ord(i)-48)            
        for j in num2:
            integer_2 = integer_2 * 10 + (ord(j) -48)
        return str(integer_1 + integer_2)