class Solution:
    def addDigits(self, n: int) -> int:
        def check(n):
            ans = 0
            for i in str(n):
                ans+=int(i)
            return ans
        while len(str(n))!=1:
            n = check(n)
        return n