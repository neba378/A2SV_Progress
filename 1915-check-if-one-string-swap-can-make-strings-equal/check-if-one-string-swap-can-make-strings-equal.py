class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        c = 0
        s = set()
        se = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c+=1
                s.add(s1[i])
                se.add(s2[i])
        if not (c == 0 or c==2):
            return False
        elif len(s)==2 and s==se:
            return True
        return False