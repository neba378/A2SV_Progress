class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n.bit_count() == 1 and n>0