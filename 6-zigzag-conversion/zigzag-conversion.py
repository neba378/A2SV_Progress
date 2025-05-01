class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        mat = [[0 for _ in range(2*n)] for _ in range(numRows)]
        if numRows == 1:
            return s
        def move(ind,i,j,down):
            if down:
                while ind<n and i<numRows:
                    mat[i][j] = s[ind]
                    ind+=1
                    i+=1
                return ind,i-2,j+1, not down
            else:
                
                while ind<n and i>=0:
                    
                    mat[i][j] = s[ind]
                    ind+=1
                    i-=1
                    j+=1
                return ind,i+2,j, not down
        ind = 0
        i,j,down = 0,0,True
        ans = []
        while ind<n:
            ind,i,j,down = move(ind,i,j,down)
        for i in range(numRows):
            for j in range(n):
                if mat[i][j]!=0:
                    ans.append(mat[i][j])
        return ''.join(ans)