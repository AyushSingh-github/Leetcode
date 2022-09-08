class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #hashing
        '''
        d={}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d[matrix[i][j]] = d.get(j,0)+1
        print(d)
            
        return True if target in d else False
        '''
        #binary search
        '''
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                l.append(matrix[i][j])
        print(l)
        
        def binary_search(l, target):
            low = 0
            high = len(l) - 1
            mid = 0
            
            while low <= high:
                mid = (high + low) // 2
                if l[mid] < target:
                    low = mid + 1   
                elif l[mid] > target:
                    high = mid - 1
                else: return True
            return False
        result = binary_search(l, target)
        
        return True if result else False
        '''
        # binarysearch based on only row and column index using matrix
        # rowindex = index/n
        #coindex = index%n
        '''If we have a matrix = [[1,2,3],[4,5,6]], rows = 2, columns = 3

Then the array will be [1,2,3,4,5,6] which means array is of length = number of rows * number of columns = 2 * 3 = 6

Lets say we want element = 4 from matrix. In that case we will get it from rowIndex = 1 and columnIndex = 0 (0-based indexing)
What about the array? We will get it from index = (rowIndex * numberOfColumns + columnIndex) => (1 * 3 + 0) => 3

What about the other way around?

If we get an element from index = 3 in an array, then if we convert that array to a n * m matrix, then what will be the row and column index in matrix for that same element?

e.g. in array = [1,2,3,4,5,6], index = 3 gives us 4

So, the same element in matrix of n * m size will be at rowIndex = (index/numberOfcolumns) = (3/3) = 1
And the columnIndex = (index % numberOfColumns) = (3 % 3) = 0

So, it means 4 will be found at matrix[1][0] which is correct for matrix = [[1,2,3],[4,5,6]]'''
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
            
        end = (rows * cols) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            row = int(mid / cols)
            col = mid % cols

            if(matrix[row][col] == target): return True
            
            if(matrix[row][col] < target):
                start = mid + 1
            else:
                end = mid - 1
                
        return False;