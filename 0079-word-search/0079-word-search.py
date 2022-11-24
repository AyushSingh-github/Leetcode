'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m = len(board[0])
        lenword = len(word)
        def backtrack(i,j,curr):
            if curr == lenword:
                return True
            if i<0 or i>=n or j<0 or j>=m or board[i][j]!=word[curr]:
                return False
            board[i][j]='#'
            res = backtrack(i-1,j,curr+1) or backtrack(i+1,j,curr+1) or backtrack(i,j-1,curr+1) or backtrack(i,j+1,curr+1) 
            board[i][j]=word[curr]
            return res
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if backtrack(i,j,0):
                        return True
        return False
'''
'''
essentially, we are trying all possibilities and checking if the word exists.
The main driver logic is the nested for loop where we are checking if a particular letter on the board matches with the first letter in the word.

If we find a match for the first letter we try all the four possibilities from that {i, j} coordinate by calling the backtrack function.

Backtracking is based on the idea of recursion so we recursively make calls every time we find a match for a letter in the word with the letter on the board and try the next four possibilities and incrementing current by 1.

We stop the recursive calls when the value of current becomes equal to the length of the word and return true since we were able to match the entire word.
We also need to stop if the i & j co-ordinates go out of bounds of the board or if we have already used a letter on the board which we check by updating the matched letters with "#" so that we do not end up matching it again for duplicate characters.


'''

#Can someone explain why my solution works when I write dfs function outside of exist function but not within exist function?

'''
class Solution:
    def dfs(self, r, c, ind, board, word, m, n):
        if r < 0 or c < 0 or r >= m or c >= n or ind >= len(word) or word[ind] != board[r][c]:
            return False

        if ind == len(word) - 1:
            return True

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for i, j in directions:
            new_r = i + r
            new_c = j + c
            temp = board[r][c]
            board[r][c] = -1

            if self.dfs(new_r, new_c, ind + 1, board, word, m, n):
                return True

            board[r][c] = temp

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, board, word, m, n):
                        return True
        
        return False


'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        R = len(board)
        C = len(board[0])
        
        # if len of word is greater than total number of character in board
        if len(word) > R*C:
            return False
        
        count = Counter(sum(board, []))
        
        # count of a LETTER in word is Greater than count of it being in board
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        # if count of 1st letter of Word(A) is Greater than that of Last One in Board(B). 
        # Reverse Search the word then search as less case will be searched.
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
                        
        # simple backtracking 
        seen = set()    # so we dont access the element again
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= R or c >= C or word[i] != board[r][c] or (r,c) in seen:
                return False
            
            seen.add((r,c))
            res = (
                dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1) 
            )
            seen.remove((r,c))  #backtracking

            return res
        
        for i in range(R):
            for j in range(C):
                if dfs(i,j,0):
                    return True
        return False