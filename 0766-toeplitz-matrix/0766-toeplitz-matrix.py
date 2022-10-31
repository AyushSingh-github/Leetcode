class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[row+1][1:] == matrix[row][:-1] for row in range(len(matrix)-1))