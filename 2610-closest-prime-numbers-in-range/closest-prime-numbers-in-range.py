class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        lst = []
        def SieveOfEratosthenes(num):
            prime = [True for i in range(num+1)]
            p = 2
            while (p * p <= num):
                if (prime[p] == True):
                    for i in range(p * p, num+1, p):
                        prime[i] = False
                p += 1
            for p in range(2, num+1):
                if prime[p] and p>=left and p<=right:
                    lst.append(p)
        SieveOfEratosthenes(right)
        mini = float("inf")
        ans = [-1,-1]
        for i in range(len(lst)-1):
            if lst[i+1] - lst[i] < mini:
                mini = lst[i+1] - lst[i]
                ans = [lst[i],lst[i+1]]
        return ans