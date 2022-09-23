class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod 
        bstr = ""
        for i in range(1,n+1):
            bstr += str(bin(i)[2:])
        return int(bstr,2)%(pow(10,9)+7)