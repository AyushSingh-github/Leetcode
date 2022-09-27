class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        res = []
        
        while left < right and top < bottom:
            #from top row = left top row -> right top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            
            #from right column = top right column -> bottom right column
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            
            #if only one row or column it will [1 - 2- 3]  or [1
            #                                                  2 
            #                                                  3]
            
            if not (left<right and top<bottom):
                break
            
            #from  bottom row = bottom right row -> bottom left row 
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            
            #from left column = bottom left column -> top left column
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            
        return res