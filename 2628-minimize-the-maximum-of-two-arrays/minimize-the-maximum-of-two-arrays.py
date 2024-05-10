class Solution:
    def minimizeSet(self, div1: int, div2: int, cnt1: int, cnt2: int) -> int:
        LCM = math.lcm(div1,div2)
        def pos(n):
            notIncluded1 = n//div1
            notIncluded2 = n//div2
            notIncluded3 = n//LCM
            return n-notIncluded1>=cnt1 and n-notIncluded2>=cnt2 and n-notIncluded3>=(cnt1+cnt2)
        l = 1
        r = 10**15
        while l<r:
            mid = (l+r)//2
            if pos(mid):
                r = mid
            else:
                l = mid+1
        return l
