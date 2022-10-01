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
        
        #We start from the top right corner of the matrix.
        row = 0
        col = len(matrix[0])-1
        
        # In this way, on the bottom side, all elements are bigger than current element
        # At left side, all elements are smaller than the current element
        
        while(row < n and col >= 0):
            mid = matrix[row][col]
            
            #If the element at this position is the target element we return True
            if(mid == target): 
                return True
            
            # If the element is smaller than this position that means, we need to go to left side of current element
            if(mid > target): 
                col -= 1
                
            #Otherwise we need to move to bottom side
            else: 
                row += 1
        
        return False