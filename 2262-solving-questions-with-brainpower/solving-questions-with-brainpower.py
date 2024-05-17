class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        dp = [0 for i in range(len(q))]
        dp[-1] = q[-1][0]
        for i in range(len(q)-2,-1,-1):
            take = q[i][0]
            if i+q[i][1]+1<len(q):
                take+=dp[i+q[i][1]+1]
            dp[i] = max(take,dp[i+1])
        return max(dp)
        