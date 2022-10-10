class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return  ""
		# this line is here so that we can replace character
		# because in python string is immutable
        s = list(palindrome)
        
		# we set idx to -1 to check if the string was all a's.
        idx = -1
        for i in range(len(s)):
            if s[i] != 'a' and i != len(s) // 2:
                idx = i
				# if we found our character we don't need to loop anymore.
                break
                
        s[idx] = 'b' if idx == -1 else 'a'
        return ''.join(s)