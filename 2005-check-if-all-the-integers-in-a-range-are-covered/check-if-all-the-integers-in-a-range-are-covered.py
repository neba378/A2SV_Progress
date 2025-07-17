class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set()
        for lst in ranges:
            for i in range(lst[0],lst[1]+1):
                s.add(i)
        s2 = set(range(left,right+1))
        return s2.issubset(s)