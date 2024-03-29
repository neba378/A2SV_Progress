class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(m,n):
            if m< n:
                (m,n) = (n,m)
            while (m % n != 0):
                (m, n) = (n, m % n)
            return n
        counter = Counter(deck)
        val = counter.values()
        res = max(val)
        for i in val:
            res = gcd(res,i)
        if res>1:
            return True
        return False
