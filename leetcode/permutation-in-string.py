class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ds1 = Counter(s1)
        ds2 = Counter()
        l, r = 0, len(s1)-1
        while r<len(s2):
            if ds1 == Counter(s2[l:r+1]):
                return True
            else:
                l+=1
                r+=1
        return False
        