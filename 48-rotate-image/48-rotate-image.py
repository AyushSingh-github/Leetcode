class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #TC = O(N2),  SC=O(1)
        #brute force
        '''
        n = len(matrix)
        m = len(matrix[0])
        
        #transpose from diagonal
        for i in range(n):
            for j in range(i+1,m):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        cols = 0
        cole = m-1
        
        #reverse row-wise  i.e. change column form 3rd to 1st and 1st to 3rd for every row
        while(cols < cole):
            for row in range(n):
                matrix[row][cols],matrix[row][cole] = matrix[row][cole],matrix[row][cols]
            cols+=1
            cole-=1
        return matrix
        '''
        
        #Striver concept
        '''
        // round 1: 
        // -------------------
        // tmp <- 1
        // top left cell matrix[i][j] (1) <- bottom left 7 cell (matrix[n - j - 1][i])
        // bottom left 7 cell (matrix[n - j - 1][i]) <- bottom right cell 9 (matrix[n - i - 1][n - j - 1])
        // bottom right cell 9 (matrix[n - i - 1][n - j - 1]) <- top right cell 3 (matrix[j][n - i - 1])
        // top right cell 3 (matrix[j][n - i - 1]) <- 1 (tmp)

        // 1 2 3    7 2 1
        // 4 5 6 => 4 5 6
        // 7 8 9    9 8 7

        // // round 2:
        // -------------------
        // tmp <- 2
        // 2 (matrix[i][j]) <- 4 (matrix[n - j - 1][i])
        // 4 (matrix[n - j - 1][i]) <- 8 (matrix[n - i - 1][n - j - 1])
        // 8 (matrix[n - i - 1][n - j - 1]) <- 6 (matrix[j][n - i - 1])
        // 6 (matrix[j][n - i - 1]) <- 2 (tmp)

        // 1 2 3    7 2 1    7 4 1
        // 4 5 6 => 4 5 6 => 8 5 2
        // 7 8 9    9 8 7    9 6 3
        '''
        n = len(matrix)
        tmp = 0
        for i in range(n//2):
            for j in range(i,n-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp
        
        