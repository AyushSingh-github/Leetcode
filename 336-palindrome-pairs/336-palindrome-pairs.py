class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {}
        for index,value in enumerate(words):
            d[value] = index
        
        result = []
        
        for index,value in enumerate(words):
            reverse = value[::-1]
            length = len(value)
            
            for i in range(length+1):
                if reverse[:i] in d and d[reverse[:i]] != d[value] and palindrome(reverse[i:]):
                    result.append((d[reverse[:i]],index))
                if reverse[i:] in d and d[reverse[i:]] != d[value] and palindrome(reverse[:i]):
                    result.append((index,d[reverse[i:]]))
        
        return set(result)
    
def palindrome(value):
    return value == value[::-1]
