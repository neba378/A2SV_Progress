class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}

        def rec(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            ans = float("inf")
            for k in range(i+1,j):
                ans = min(ans,values[i]*values[j]*values[k]+rec(i,k)+rec(k,j))
            if ans == float("inf"):
                memo[(i,j)] = 0
            else:
                memo[i,j] = ans
            return memo[i,j]
        return rec(0,len(values)-1)