class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x
        c = 0
        while i<=j:
            mid = (i+j)//2
            mdsqr = mid*mid
            
            if mdsqr == x:
                return mid
            elif mdsqr < x:
                c = max(c,mid)
                i = mid+1
            else:
                j = mid-1
        return c




           
        