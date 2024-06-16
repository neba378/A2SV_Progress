class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = bin(n)[2:]
        for i in range(len(x)-1):
            if x[i] != x[i+1]:
                continue
            else:
                return False
        return True