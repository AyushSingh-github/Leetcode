class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        #transpose
        for i in range(n):
            for j in range(i+1,m):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        cols = 0
        cole = m-1
        
        #reverse
        while(cols < cole):
            for row in range(n):
                matrix[row][cols],matrix[row][cole] = matrix[row][cole],matrix[row][cols]
            cols+=1
            cole-=1
        return matrix