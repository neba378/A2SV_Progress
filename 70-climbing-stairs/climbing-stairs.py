class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {}
        ans = 0
        def rec(m):
            nonlocal ans
            if m>n:
                return 0
            if m==n:
                return 1
            if m not in dic:
                dic[m] = rec(m+1) + rec(m+2)
            return dic[m]
        
        return rec(0)
