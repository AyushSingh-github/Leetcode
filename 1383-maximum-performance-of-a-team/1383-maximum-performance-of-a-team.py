class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for eff,spd in zip(efficiency,speed):
            eng.append([eff,spd])
        
        #soring based on eff to get max to min eff
        eng.sort(reverse=True)
        #print(eng)
        
        maxPerformance,currspeed = 0,0
        minHeap = []
        
        for eff,spd in eng:
            #if total spd of eng is more than K required then pop from heap and then reduce the total currspeed  till the K eng spd
            if len(minHeap)==k:
                currspeed -= heapq.heappop(minHeap)
                #print(currspeed)
            
            # else keep incr the total speed of the eng and then push in the heap to get the mini eff amoang the eng but getting max Performance by max total eng speed     
            currspeed += spd
            heapq.heappush(minHeap,spd)
            #maxi of prev Performance and the curr performance by the spd of top pop enfg speed 
            maxPerformance = max(maxPerformance, eff*currspeed)
            #print(eff*currspeed)
            
        return maxPerformance % (10**9 + 7)
            

            