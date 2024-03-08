class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def myPow(x,n):
            if n==1:
                return x 
            if n==0:
                return 1
            
            if n%2 == 0:
                ans = myPow(x,n//2)%(1000000007)
                return ans**2
            else:
                ans = myPow(x,n//2)%(1000000007)
                return ans**2*x

        if n%2 == 0:
            return (myPow(5,n//2) * myPow(4,n//2))%(1000000007)
        else:
            return (myPow(5,n//2+1) * myPow(4,n//2))%(1000000007)
        