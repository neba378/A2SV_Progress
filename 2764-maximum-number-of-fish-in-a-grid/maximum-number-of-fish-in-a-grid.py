
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        DIR = [(0,1),(1,0),(0,-1),(-1,0)]
        def isBound(r,c):
            return 0<=r<row and 0<=c<col
        dic = {}
        ans = []
        def dfs(i,j,mid):
            if grid[i][j] == 0:
                return 0
            mid = grid[i][j]
            dic[(i,j)] = 0
            for dx,dy in DIR:
                if isBound(i+dx,j+dy) and (i+dx,j+dy) not in dic:
                    mid+=dfs(i+dx,j+dy,mid)
            ans.append(mid)
            return mid
        for r in range(row):
            for c in range(col):
                dfs(r,c,0)
        if ans == []:
            return 0
        return max(ans)
        # graph = defaultdict(list)
        # for r in range(row):
        #     for c in range(col):
        #         for dx,dy in DIR:
        #             if grid[r][c] !=0:
        #                 if isBound(r+dx,c+dy) and grid[r+dx][c+dy]:
        #                     graph[(r,c)].append((r+dx,c+dy))
        #                     graph[(r+dx,c+dy)].append((r,c))
        # vis = {}
        # ans = []
        # print(graph)
        # def dfs(pos,s):
        #     vis[pos] = 0
        #     s+=grid[pos[0]][pos[1]]
        #     for ngh in graph[pos]:
        #         if ngh not in vis:
        #             dfs(ngh,s)
        #     ans.append(s)
        # for pos in graph:
        #     dfs(pos,0)
        # print(ans)
        # return 8
            
        

                

        