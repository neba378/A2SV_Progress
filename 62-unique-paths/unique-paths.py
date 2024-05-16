class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        # def inbound(i,j):
        #     return 0<=i<m and 0<=j<n
        # def dp(i,j):
        #     if i == m-1 or j == n-1:
        #         return 1
        #     if inbound(i,j):
        #         if (i,j) not in memo:
        #             memo[(i,j)] = dp(i+1,j)+dp(i,j+1)
        #         return memo[(i,j)]
        #     else:
        #         return 0
        # return dp(0,0)
            
        dp = [[0 for i in range(n)] for j in range(m)]
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r==m-1 or c == n-1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r+1][c]+dp[r][c+1]
        return dp[0][0]