class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        
        freq = set()
        
        for _,value in count.items():
            if value in freq:
                return False
            freq.add(value)
        return True