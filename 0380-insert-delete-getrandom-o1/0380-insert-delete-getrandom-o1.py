class RandomizedSet:

    def __init__(self):
        self.frequency = set()

    def insert(self, val: int) -> bool:
        if val not in self.frequency:
            self.frequency.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.frequency:
            self.frequency.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        item = random.choice(list(self.frequency))
        return item 
   

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()