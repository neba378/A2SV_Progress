class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n-1,-1,-1):
            if obstacleGrid[-1][i] == 0:
                dp[-1][i] = 1
            else:
                break
        for i in range(m-1,-1,-1):
            if obstacleGrid[i][-1] == 0:
                dp[i][-1] = 1
            else:
                break
        for r in range(m-2,-1,-1):
            for c in range(n-2,-1,-1):
                if r==m-1 or c == n-1 and obstacleGrid[r][c] == 0:
                    dp[r][c] = 1
                else:
                    if obstacleGrid[r][c] == 0:
                        dp[r][c] = dp[r+1][c]+dp[r][c+1]
                    
        return dp[0][0]