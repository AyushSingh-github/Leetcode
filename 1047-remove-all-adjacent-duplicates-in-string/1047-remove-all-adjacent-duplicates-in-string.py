from collections import deque

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        
        for i in range(len(s)):
            if (stack and stack[-1] == s[i]):
                stack.pop()
            else:
                stack.append(s[i])
                
        return "".join(stack)
    
class Solution:
    def removeDuplicates(self, s: str) -> str:
        return reduce(lambda chars_stack, char:chars_stack[:-1] if chars_stack[-1:] == char else chars_stack + char, s)    