class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([words[::-1] for words in s.split()])