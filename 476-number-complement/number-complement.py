class Solution:
    def findComplement(self, num: int) -> int:
        b = len(bin(num)[2:])
        tot = 2**b-1
        return tot^num
