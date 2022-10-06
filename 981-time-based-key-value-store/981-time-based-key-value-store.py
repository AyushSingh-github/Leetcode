'''
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
            m = (l + r) // 2
            if timeValues[m][1] == timestamp:
                return timeValues[m][0]

            elif timeValues[m][1] < timestamp:
                ans = timeValues[m][0]
                l = m + 1
            
            else:
                r = m - 1

        return ans
'''
class TimeMap:

    def __init__(self):
		# Creating a default dictionary using collections package (build-in package)
        self.dictionary = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
		# appending (value, timestamp) tuple to the list associated to the key
		# Remember this is a defaultdict with default value as list. So each key has an empty list which does not exist in the hash table
		# Therefore, we directly appended the tuple without checking whether the key exist or not.
        self.dictionary[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
		# Accessing the list associated with the key.
        data = self.dictionary[key]
		# If the key does not exist in our hash table, we will return ""
        if not data: return ""
		# Going through each timestamp in reverse order and check the below condition
		# timestamp_prev <= timestamp
		# if this condition is satisfied, we simply return the value associated with that perticular tuple
        for val,time in reversed(data):
            if time <= timestamp:
                return val
		# else at the end no timestamp exist in the list which is less than the given timestamp, so we return
        return ""
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)