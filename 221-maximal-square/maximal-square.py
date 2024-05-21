class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def mult(mat,i,j):
            return not "0" in {mat[i][j],mat[i][j-1],mat[i-1][j],mat[i-1][j-1]}
       
        row = len(matrix)
        col = len(matrix[0])
        maxi = 0
        for r in range(row):
            for c in range(col):
                maxi = max(int(matrix[r][c]),maxi)
        for r in range(1,row):
            for c in range(1,col):
                if mult(matrix,r,c):
                    matrix[r][c] = min(int(matrix[r - 1][c - 1]),int(matrix[r - 1][c]),int(matrix[r][c - 1])) + 1
                    maxi = max(maxi,matrix[r][c])
        return maxi**2

