class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [(1,0),(0,1),(-1,0),(0,-1)]
        def isbound(r,c,row,col):
            return 0<=r<row and 0<=c<col
        row = len(grid)
        col = len(grid[0])
        def dfs(r,c):
            
            if (r,c) not in visited:
                visited.add((r,c))
            
            for dx,dy in DIR:
                nx = r+dx
                ny = c+dy
                if isbound(nx,ny,row,col):
                    if grid[nx][ny] == "1" and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        dfs(nx,ny)
                    
                        
                else:
                    continue


        visited = set()
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
        return count
                
                    