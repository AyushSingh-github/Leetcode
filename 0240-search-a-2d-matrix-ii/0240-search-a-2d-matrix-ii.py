class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ''' 
        row=len(matrix)
        b=False
        col=len(matrix[0])
        r1=0
        r2=row-1
        c1=0
        c2=col-1
        #mid=(c1+c2)//2
        while(r1<=r2 and c1<=c2):
            mid=(c1+c2)//2
            if matrix[r1][mid]==target:
                return True
            b=True
            if (matrix[r1][mid]>target):
                c2=mid-1
            else:
                c2=mid+1
                r1=r1+1
        return b
        '''
        
        n = len(matrix)
        #start from the top right [row][col] point of the matrix.
        row = 0
        col = len(matrix[0])-1
        
        while(row < n and col >= 0):
            mid = matrix[row][col]
            
            if(mid == target): 
                return True
            
            if(mid > target): 
                col -= 1
            else: 
                row += 1
        
        return False