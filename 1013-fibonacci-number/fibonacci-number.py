class Solution:
    def fib(self, n: int) -> int:
        dic = {1: 1, 0: 0}
        if n == 0:
            return 0
        s = 0
        for i in range(n-1):
            if i in dic:
                s += dic[i]
            else:
                dic[i] = dic[i-1]+dic[i-2]
                s += dic[i]
        return s+1