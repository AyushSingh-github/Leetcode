class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        d={}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d[matrix[i][j]] = d.get(j,0)+1
        print(d)
            
        return True if target in d else False
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
 