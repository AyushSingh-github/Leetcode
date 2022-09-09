class Solution:
    def firstUniqChar(self, s: str) -> int:
        for val in s:
            if s.count(val)==1:
                return s.index(val)
        return -1
                