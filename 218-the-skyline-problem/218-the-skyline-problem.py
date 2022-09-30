class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x[0])
        res = 0
        heap, l_heap = [], 0
        for interval in intervals:
            while heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
                l_heap -= 1
            heapq.heappush(heap, interval[1])
            l_heap += 1
            res = max(res, l_heap)
        return res
	
    inf = 999999
    def getSkyline(self, buildings):
        buildings.append([float('inf'), float('inf'), 0])
        heap = []
        key_points = []
        curr_max = 0
        for Li, Ri, Hi in buildings:
            while heap and heap[0][0] < Li:
                ri, hi = heapq.heappop(heap)
                heap_max = 0
                for j in range(len(heap)):
                    heap_max = max(heap_max, heap[j][1])
                if heap_max < curr_max:
                    curr_max = heap_max
                    key_points.append([ri, curr_max])
            if Hi > curr_max:
                if key_points and Li == key_points[-1][0]:
                    key_points.pop()
                key_points.append([Li, Hi])
                curr_max = Hi
            heapq.heappush(heap, (Ri, Hi))
        return key_points
