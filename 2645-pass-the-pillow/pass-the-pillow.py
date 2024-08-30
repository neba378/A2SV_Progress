class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cyc = (n-1)*2
        mod = time%cyc
        if mod<n:
            return mod+1
        return 2*n-1-mod