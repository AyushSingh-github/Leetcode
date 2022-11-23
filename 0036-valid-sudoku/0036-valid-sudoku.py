'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowSet = set()
            for val in row:
                if val == '.':
                    continue
                if val in rowSet:
                    return False
                rowSet.add(val)
        
        for j in range(len(board[0])):
            colSet = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in colSet:
                    return False
                colSet.add(board[i][j])
                
        for iStart in range(0, len(board), 3):
            for jStart in range(0, len(board[0]), 3):
                dreiSet = set()
                for i in range(iStart, iStart + 3):
                    for j in range(jStart, jStart + 3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in dreiSet:
                            return False
                        dreiSet.add(board[i][j])
        return True
        
'''        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            numbers = [n for n in row if n != '.']
            if len(set(numbers)) != len(numbers):
                return False

        for i in range(9):
            numbers = [board[j][i] for j in range(9) if board[j][i] != '.']
            if len(set(numbers)) != len(numbers):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                numbers = [board[x+i][y+j]
                           for x in range(3) for y in range(3)
                           if board[x+i][y+j] != '.']
                if len(set(numbers)) != len(numbers):
                    return False
        
        return True        
               
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # a function to check rows, cols and blocks
        def is_valid(digits):
            return len(set(s:= [d for d in digits if d != "."])) != len(s)
    
        # a generator to extract blocks
        def blocks():
            for i in range(3):
                for j in range(3):
                    yield [n for row in board[i*3:(i+1)*3] for n in row[j*3:(j+1)*3]]
    
        if any(map(is_valid, board))       : return False       # [1] test rows
        if any(map(is_valid, zip(*board))) : return False       # [2] test cols
        if any(map(is_valid, blocks()))    : return False       # [3] test blocks
    
        return True
'''