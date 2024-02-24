class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        ans = []
        for i in points:
            lst.append((i[1]**2 + i[0]**2,i))
        lst.sort()
        for i in range(k):
            ans.append(lst[i][1])
        return ans
        