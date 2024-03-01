class Solution:
    def minimumSteps(self, s: str) -> int:
        cZ = 0
        cO = 0
        counter = Counter(s)
        sumy = 0
        for i in range(len(s)):
            if s[i] == '1':
                cO+=1
                sumy+=(counter['0']-cZ)
            if s[i] == '0':
                cZ+=1
        return sumy
