class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        if stones[1] - stones[0] != 1:
            return False
        for stone in stones:
            dp[stone] = set()
        dp[stones[1]].add(1)
        for i in range(1, len(stones)):
            for j in dp[stones[i]]:
                if stones[i]+j-1 in dp and stones[i]+j-1 != stones[i]:
                    dp[stones[i] + j - 1].add(j - 1)
                if stones[i] + j in dp:
                    dp[stones[i] + j].add(j)
                if stones[i] + j + 1 in dp:
                    dp[stones[i] + j + 1].add(j + 1)
        return dp[stones[-1]]

