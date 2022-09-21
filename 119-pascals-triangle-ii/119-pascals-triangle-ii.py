class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # TC =O(N2)
        '''
        res = [1]
        for i in range(rowIndex):
            res = [0] + res
            for j in range(len(res) - 1):
                res[j] = res[j] + res[j+1]
        return res
        '''

		# Nth Row of Pascal Triangle - nC0 , nC1, nC2 .......   nCn
        #Striver Concept
        #TC = O(N)
        li=[1]
        res = 1
        for i in range(rowIndex):
            res *= (rowIndex - i)
            res /= (i+1)
            li.append(int(res))
        return li