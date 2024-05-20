class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        n=len(tri)
        dp=[[0] * (n+1) for _ in range(n+1)]
        for l in range(n-1,-1,-1):
            for i in range(l+1):
                dp[l][i]=tri[l][i] + min(dp[l+1][i], dp[l+1][i+1])
        return dp[0][0]            