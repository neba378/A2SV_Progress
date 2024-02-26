class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        tot = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                s1 = sum(grid[i][j:j+3])
                s2 = sum(grid[i+2][j:j+3])
                m = grid[i+1][j+1]
                now = s1+s2+m
                tot = max(tot,now)
        return tot
                    
