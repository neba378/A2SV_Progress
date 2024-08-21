class Solution:
    def monkeyMove(self, n: int) -> int:
        memo = {1:2,2:4}
        def rec(n):
            if n in memo:
                return memo[n]
            if n%2 == 1:
                memo[n] = rec(n//2) * rec((n//2)+1)%1000000007
            else:
                memo[n] = rec(n//2) * rec(n//2)%1000000007
            return memo[n]
        rec(n)
        return (memo[n]-2)%1000000007