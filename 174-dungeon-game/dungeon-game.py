class Solution:
    def calculateMinimumHP(self, d: List[List[int]]) -> int:
        m = len(d)
        n = len(d[0])
        dp = [[0]*n for i in range(m)]
        dp[-1][-1] = max(1,1-d[-1][-1])
        for i in range(m-2,-1,-1):
            dp[i][-1] = max(1,dp[i+1][-1]-d[i][-1])
        for i in range(n-2,-1,-1):
            dp[-1][i] = max(1,dp[-1][i+1]-d[-1][i])
        for r in range(m-2,-1,-1):
            for c in range(n-2,-1,-1):
                dp[r][c] = max(1,min(dp[r+1][c]-d[r][c],dp[r][c+1]-d[r][c]))
        return dp[0][0]

        