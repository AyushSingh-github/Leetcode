class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        rowlist = self.generate(numRows-1)
        lastrow = rowlist[-1]
        rowlist.append( [1] + [lastrow[i] + lastrow[i-1] for i in range(1, len(lastrow))] + [1] )
        
        return rowlist