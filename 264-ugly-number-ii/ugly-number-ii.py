class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        i2 = i3 = i5 = 0
        ugly[0] = 1
        
        for i in range(1, n):
            next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            ugly[i] = next_ugly
            
            if next_ugly == ugly[i2] * 2: i2 += 1
            if next_ugly == ugly[i3] * 3: i3 += 1
            if next_ugly == ugly[i5] * 5: i5 += 1
            
        return ugly[n-1]
