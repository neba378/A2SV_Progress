class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lst = []
        lst2 = []
        for ch in s:
            lst.append(s.index(ch))
        for ch in t:
            lst2.append(t.index(ch))
        if lst == lst2:
            return True
        return False