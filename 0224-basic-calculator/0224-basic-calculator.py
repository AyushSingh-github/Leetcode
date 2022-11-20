class Solution:
    def calculate(self, s: str) -> int:
        def calc(left, op, right):
            if op == '+':
                return left + right
            if op == '-':
                return left - right


        def parse_str(s, i = 0):
            left = 0
            op = '+'
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                elif s[i].isnumeric():
                    nb = 0
                    while i < len(s) and s[i].isnumeric():
                        nb *= 10
                        nb += ord(s[i]) - ord('0')
                        i += 1
                    if op:
                        left = calc(left, op, nb)
                        op = None
                    else:
                        left = nb
                elif s[i] in ['+', '-']:
                    op = s[i]
                    i += 1
                elif s[i] == '(':
                    nb, i = parse_str(s, i + 1)
                    left = calc(left, op, nb)
                elif s[i] == ')':
                    return left, i + 1
            return left
        return parse_str(s)   
        
        
'''       
class Solution:
    def calculate(self, s: str) -> int:
    output, curr, sign , stack = 0,0,1,[]
    
        for ch in s:
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            elif ch in "+-":
                output += (curr * sign)
                curr = 0
                if ch == "-":
                    sign = -1
                else:
                    sign = 1
            elif ch =="(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif ch == ")":
                output += curr*sign
                output *= stack.pop()
                output += stack.pop()
                curr = 0
        return output +(curr*sign)
       

'''
#not working
'''
class Solution:
    def calculate(self, s: str) -> int:
        index = 0
        result,temp = 0,0
        digits = '&'
        isFinish = False
        while(index < len(s) and not isFinish):
            if(s[index] == '+' or s[index] == '-'):
                if (digits == '-'):
                    temp *= -1
                result += temp
                digits = s[index]
                temp = 0
                index+=1
                
            elif (s[index] == '(' ):
                index+=1
                temp = self.calculate(s)
                if(digits == '-'):
                    temp *= -1
                result += temp
                temp = 0
                digits = '&'
                
            elif(s[index] == ')'):
                if(digits == '-'):
                    temp *= -1
                result += temp
                temp = 0
                digits = '&'
                isFinish = True
                index+=1
            
            elif(s[index] != ' '):
                if(temp != 0):
                    temp *= 10
                temp += (int(s[index]) - 0)
                index+=1
            
            else:
                index+=1
        
        if(index == len(s) and temp != 0):
            if(digits == '-'):
                temp *= -1
            result += temp
        
        return result
'''    
