class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIC = [(1,0), (-1,0), (0,1), (0,-1)]
         
        rows = len(grid)
        if rows == 0:  
            return -1
        cols = len(grid[0])
        fresh = 0
        rotten = deque()
        def isBound(r,c):
            return 0<=r<rows and 0<=c<cols
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                        rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        ans = 0
        while rotten and fresh > 0:
            ans += 1
            
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in DIC:
                    xx, yy = x + dx, y + dy
                    if not isBound(xx,yy):
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    fresh -= 1
                    
                    grid[xx][yy] = 2
                    
                    rotten.append((xx, yy))

        return ans if fresh == 0 else -1