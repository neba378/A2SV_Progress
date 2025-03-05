class Solution:
    def coloredCells(self, n: int) -> int:
        def rec(n):
            if n == 1:
                return 1
            return rec(n-1)+(n-1)*4
        return rec(n)