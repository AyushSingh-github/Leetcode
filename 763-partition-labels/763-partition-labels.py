class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        print(d)
        ar = []
        maxx = -1
        for i in range(len(s)):
            if maxx < d[s[i]]:
                maxx = d[s[i]]
                print(maxx,i)
            if i == maxx:
                ar.append(i+1)
        print("array till new string is sliced",ar)
        for i in range(len(ar)-1,0,-1):
            ar[i]=ar[i]-ar[i-1]
        print("after deletion",ar)
        return ar