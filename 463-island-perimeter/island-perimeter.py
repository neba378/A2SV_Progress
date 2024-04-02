class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]


        # def inbound(row, col):
        #     return (0 <= row < len(grid) and 0 <= col < len(grid[0]))


        # def dfs(grid, visited, row, col):
        #     # base case
        #     visited[row][col] = True
        #     for row_change, col_change in directions:
        #         new_row = row + row_change
        #         new_col = col + col_change
        #         if inbound(new_row, new_col) and not visited[new_row][new_col]:
        #             dfs(grid, visited, new_row, new_col
        minimize = 0
        for row in range(len(grid)):
            for col in range(1,len(grid[0])):

                if grid[row][col] == grid[row][col-1] == 1:
                    print(row,col," ",row,col-1)
                    minimize -=2
        for col in range(len(grid[0])):
            for row in range(1,len(grid)):
                if grid[row][col] == grid[row-1][col] == 1:
                    print(row,col," ",row-1,col)
                    minimize -=2
        tp = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    tp+=4
        return tp+minimize
        