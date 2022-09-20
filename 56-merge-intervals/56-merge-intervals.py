class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans= []
        
        #previous interval 1st and 2nd value and compare with next interval 1st value and then 2nd value
        low = intervals[0][0]
        high =  intervals[0][1]
        for i in range(1,len(intervals)):
            if low <= intervals[i][0] <= high and intervals[i][1] >= high:
                high = intervals[i][1]
            elif low <= intervals[i][0] <= high and intervals[i][1] < high:
                continue
            else:
                ans.append([low,high])
                low = intervals[i][0]
                high = intervals[i][1]
        ans.append([low,high])
        return ans