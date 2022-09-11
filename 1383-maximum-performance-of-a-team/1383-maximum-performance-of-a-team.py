class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for eff,spd in zip(efficiency,speed):
            eng.append([eff,spd])
            
        eng.sort(reverse=True)
        print(eng)
        
        maxPerformance,currspeed = 0,0
        minHeap = []
        
        for eff,spd in eng:
            if len(minHeap)==k:
                currspeed -= heapq.heappop(minHeap)
                print(currspeed)
                
            currspeed += spd
            heapq.heappush(minHeap,spd)
            maxPerformance = max(maxPerformance, eff*currspeed)
            #print(eff*currspeed)
            
        return maxPerformance % (10**9 + 7)
            

            