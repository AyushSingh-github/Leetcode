class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        #not working
        '''
        rows = len(grid)
        cols = len(grid[0])
        
        def helper(x,y,k,visited):
            if k < 0 or x < 0 or y < 0 or x >= rows or y >= cols:
                return float('inf')
            
            if x == rows-1 and y == cols-1:
                return 0
            
            dirs = [0,1,0,-1,0]
            minSteps = float('inf')
            
            if grid[x][y]==1:
                k -= 1
            res = float('inf')
            visited[(x,y)] = k
            
            for i in range(4):
                new_x, new_y = x + dirs[i], y + dirs[i+1]
                if (new_x,new_y) not in visited or visited[(new_x,new_y)] < k:
                    res = min(res, 1 + helper(new_x,new_y,k,visited))
            return res
        
        result=helper(0,0,k,{})
        
        return result if result != float('inf') else -1
    
    
        '''
        m, n = len(grid), len(grid[0])
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        
        # in vis list, we will store "number of obstacles we can still remove" further
        visited = [[-1]*n for _ in range(m)]
        
        # x, y, current steps, number of obstacles we can still remove
        q = collections.deque([(0,0,0,k)])
        while q:
            x, y, steps, obst = q.popleft()
            
            # Exit if current position is outside of the grid
            if x<0 or y<0 or x>=m or y>=n:
                continue
                
            # Destination Found
            if x==m-1 and y==n-1:  
                return steps
            
            if grid[x][y]:
                if obst:
                    obst-=1
                else: # Exit if we encounter obstacle and we can not remove it
                    continue
                    
            # Exit currentt path, if cell was visited and in previous path it was able to remove more number of obstacles further,
            # means it had more chane to reach destination
            if visited[x][y]!=-1 and visited[x][y]>=obst:
                continue
            visited[x][y]=obst
            
            for dx, dy in directions:
                q.append((x+dx,y+dy,steps+1,obst))      
        return -1
        