class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        t = 0
        ans = []
        if m*n != len(original):
            return ans
        for i in range(m):
            lst = []
            for j in range(n):
                lst.append(original[t])
                t+=1
            ans.append(lst)
        return ans