class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def digitSum(n):
            ans = 0 
            for i in n:
                ans+=int(i)
            return ans
        def solve(s,k):
            ans = []
            i = 0
            while i< (len(s)):
                s1 = digitSum(s[i:i+k])
                i+=k
                ans.append(str(s1))
            return "".join(ans)
        while len(s) > k:
            s = solve(s,k)
        return s
                