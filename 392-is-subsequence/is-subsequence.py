class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        dp = [[0 for i in range(T+1)] for i in range(S+1)]
        for i in range(S):
            for j in range(T):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        print(dp)
        return dp[-1][-1] == len(s)