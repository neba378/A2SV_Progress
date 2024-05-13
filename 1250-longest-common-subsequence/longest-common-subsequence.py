class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        memo = {}
        def dp(i,j):
            if i>=len(t1) or j>=len(t2):
                return 0
            if (i,j) not in memo:
                if t1[i] == t2[j]:
                    memo[(i,j)] = 1+dp(i+1,j+1)
                elif t1[i]!=t2[j]:
                    memo[(i,j)] = max(dp(i,j+1),dp(i+1,j))
            return memo[(i,j)]
        return dp(0,0)
            