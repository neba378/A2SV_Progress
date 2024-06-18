class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x 
        if n==0:
            return 1
        if n == -1:
            return 1/x
        if n%2 == 0:
            ans = self.myPow(x,n//2)
            return ans**2
        else:
            ans = self.myPow(x,n//2)
            return ans**2*x
        