#TLE
'''
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=len(maze),len(maze[0])
        visited=set()
        queue=deque([(entrance[0],entrance[1],0)])
        while queue:
            i,j,steps=queue.popleft()
            visited.add((i,j))
            for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                ni,nj=i+di,j+dj
                if 0<=ni<m and 0<=nj<n and  maze[ni][nj]=="." and (ni,nj) not in visited:
                    if ni==0 or nj==0 or ni==m-1 or nj==n-1: return steps+1
                    queue.append([ni,nj,steps+1])
        return -1 
'''

'''
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        r,c = entrance
        queue = deque([(r,c,0)])
        visited = set([(r,c)])
        
        while queue:
            r,c,d = queue.popleft()
            
            if d != 0 and (r + 1 == ROWS or r - 1 == -1 or c + 1 == COLS or c - 1 == -1):
                return d
            
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr,nc = r+dr, c+dc
                
                if ROWS > nr >= 0 <= nc < COLS and maze[nr][nc] != '+' and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,d+1))
        
        return -1

'''
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # Mark the entrance as visited since its not a exit.
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        
        # Start BFS from the entrance, and use a queue `queue` to store all 
        # the cells to be visited.
        queue = collections.deque()
        queue.append([start_row, start_col, 0])
        
        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()
            
            # For the current cell, check its four neighbor cells.
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                
                # If there exists an unvisited empty neighbor:
                if 0 <= next_row < rows and 0 <= next_col < cols \
                    and maze[next_row][next_col] == ".":
                    
                    # If this empty cell is an exit, return distance + 1.
                    if 0 == next_row or next_row == rows - 1 or 0 == next_col or next_col == cols - 1:
                        return curr_distance + 1
                    
                    # Otherwise, add this cell to 'queue' and mark it as visited.
                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])
            
        # If we finish iterating without finding an exit, return -1.
        return -1