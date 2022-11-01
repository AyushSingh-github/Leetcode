class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        #dfs
        #TC ->  O(m.n)
        
        def findBallColumn(row,col,grid):
            if (row==len(grid)):
                return col
            nextCol = col + grid[row][col]
            if nextCol < 0 or nextCol > len(grid[0])-1 or grid[row][col] != grid[row][nextCol]:
                return -1
            return findBallColumn(row+1,nextCol,grid)
        
        
        result = [0]*len(grid[0])
        #print(result)
        for i in range(len(grid[0])):
            result[i] = findBallColumn(0,i,grid)
            
        return result
    
