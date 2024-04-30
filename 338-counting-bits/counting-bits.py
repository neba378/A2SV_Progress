class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        c = 0
        for i in range(n+1):
            c = 0
            pre = n
            while n!=0:
                c += n&1
                n >>= 1
            n = pre-1
            ans.append(c)
        return reversed(ans)
