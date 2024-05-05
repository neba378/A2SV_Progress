class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b & 0xffffffff: 
            c = a & b
            a = a ^ b
            b = c << 1
        return a & 0xffffffff if b > 0xffffffff else a