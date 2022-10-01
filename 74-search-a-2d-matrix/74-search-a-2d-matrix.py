class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        row = 0
        col = len(matrix[0])-1
        
        while(row < n and col >= 0):
            mid = matrix[row][col]
            if(mid == target): return True
            if(mid > target): col -= 1
            else: row += 1
        
        return False