class Solution:
    def tribonacci(self, n: int) -> int:
        dic = {1:1,0:0,2:1}
        def rec(n):
            if n<=1:
                return n
            if n == 2:
                return 1
            if n not in dic:
                dic[n] = rec(n-3)+rec(n-2)+rec(n-1)
            return dic[n]
        return rec(n)