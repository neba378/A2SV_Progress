class Solution:
    def integerBreak(self, num: int) -> int:
        memo = {1:1}
        def rec(n):
            if n in memo:
                return memo[n]
            memo[n] = 0 if n==num else n
            for i in range(1,n):
                val = rec(i)*rec(n-i)
                memo[n] = max(memo[n],val)
            return memo[n]
        return rec(num)