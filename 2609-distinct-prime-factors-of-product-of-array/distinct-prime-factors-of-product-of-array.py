class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primefactor(n):
            fact = set()
            fact.add(1)
            d = 2
            while d**2<=n:
                while n%d == 0:
                    fact.add(d)
                    n//=d
                d+=1
            if n>1:
                fact.add(n)
            
            return fact
        s = set()
        for i in range(len(nums)):
            for j in primefactor(nums[i]):
                s.add(j)
        return len(s)-1
        
        