class TimeMap:

    def __init__(self):
        self.hashmap = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        timeValues = self.hashmap.get(key, [])
        l, r = 0, len(timeValues) - 1
        while l <= r:
            m = int((l + r) / 2)
            if timeValues[m][1] == timestamp:
                return timeValues[m][0]

            elif timeValues[m][1] <= timestamp:
                ans = timeValues[m][0]
                l = m + 1
            
            else:
                r = m - 1

        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)