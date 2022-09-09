class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

            