class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        i = 1
        j = max(p)
        c = -1
        while i<=j:
            mid = i+(j-i)//2
            calc = 0
            for _ in range(len(p)):
                calc+=ceil(p[_]/mid)
            if calc > h:
                i = mid+1
            else:
                j = mid-1
                c = mid
        return c
            