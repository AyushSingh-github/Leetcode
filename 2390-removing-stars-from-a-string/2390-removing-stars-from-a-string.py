'''
from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        ans = deque()
        for x in s:
            if x!='*':
                ans.append(x)
            else:
                ans.pop()
        return ''.join(ans)
    
'''
class Solution:

    def removeStars(self, s: str) -> str:
        # return self.two_pointer_method(s)
        return self.stack_method(s)

    @staticmethod
    def stack_method(s: str) -> str:
        push, pop = (stk := deque()).append, stk.pop

        for c in s:
            if c == '*':
                pop()
            else:
                push(c)

        return ''.join(stk)

    @staticmethod
    def two_pointer_method(s: str) -> str:
        k, A = 0, list(s)

        for i, c in enumerate(s):
            if c == '*':
                k -= 1
            else:
                A[k] = c
                k += 1

        return ''.join(A[:k])
