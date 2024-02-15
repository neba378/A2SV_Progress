class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        c = 0
        l = len(mat)
        for i in range(l):
            c+= mat[i][i]
            c+=mat[i][l-1-i]
        if l%2 == 0:
            return c
        return c-mat[l//2][l//2]