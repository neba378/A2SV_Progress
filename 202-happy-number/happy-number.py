class Solution:
    def isHappy(self, n: int) -> bool:
        def check(n):
            ans = 0
            for i in str(n):
                ans+=int(i)**2
            return ans
        dic = {}
        while n not in dic:
            dic[n] = 0
            if n == 1:
                return True
            n = check(n)
        return False