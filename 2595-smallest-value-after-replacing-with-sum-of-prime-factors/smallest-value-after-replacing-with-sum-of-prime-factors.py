class Solution:
    def smallestValue(self, n: int) -> int:
        def primefactor(n):
            fact = []
            d = 2
            while d**2 <= n:
                while n % d == 0:
                    fact.append(d)
                    n //= d
                d += 1
            if n > 1:
                fact.append(n)

            return fact

        def isPrime(n):
            d = 2
            if n == 1:
                return False
            while d**2 <= n:
                if n % d == 0:
                    return False
                d += 1
            return True

        while not isPrime(n) and n!=4:
            n = sum(primefactor(n))
        return n
