class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        prev = ans = 0
        
        d = []
        for grow, plant in zip(growTime, plantTime):
            d.append([grow,plant])
        d.sort(key = lambda x:-x[0])
        #print(d)
        
        for grow,plant in d:
            ans = max(ans,grow + plant + prev)
            prev += plant
        return ans