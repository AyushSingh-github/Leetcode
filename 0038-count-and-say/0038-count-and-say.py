class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        update = self.countAndSay(n-1)
        s=""
        start = update[0]
        count =1
        for i in range(1,len(update)):
            if update[i]==start:
                count+=1
            else:
                s += str(count) + str(start)
                start=update[i]
                count=1
                
        s += str(count) + str(start)
        return s