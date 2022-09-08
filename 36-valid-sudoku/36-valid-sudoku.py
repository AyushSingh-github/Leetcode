class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) 
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) 
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if(board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares [(i//3,j//3)]): return False
                    
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
        return True
    
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols,square = {},{},{}
        
        # for each rows value
        for i in range(len(board)): 
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if i in rows:
                        if board[i][j] not in rows[i]:
                            rows[i].add(board[i][j])
                        else: return False
                    else:
                        rows[i] = set(board[i][j])
                        
                    if j in cols:
                        if board[i][j] not in cols[j]:
                            cols[j].add(board[i][j])
                        else: return False
                    else:
                        cols[j] = set(board[i][j])
                        
                    boxvalue = i//3 + (j//3)*3
                    
                    if boxvalue in square:
                        if board[i][j] not in square[boxvalue]:
                            square[boxvalue].add(board[i][j])  
                        else: return False
                    else:
                        square[boxvalue] = set(board[i][j])
        return True
'''