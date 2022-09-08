class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        d={}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d[matrix[i][j]] = d.get(j,0)+1
        print(d)
            
        return True if target in d else False
        