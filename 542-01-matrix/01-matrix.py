class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(r,c,row,col):
            return 0<=r<row and 0<=c<col
        ans = [[float("inf") for _ in range(len(mat[0]))] for i in range(len(mat))]
        row = len(mat)
        col = len(mat[0])
        queue = deque()
        for r in range(row):
            for c in range(col):
                if mat[r][c]==0:
                    ans[r][c] = 0
                    queue.append((r,c))
        print(queue)
        DIR = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            r,c = queue.popleft()
            for dx,dy in DIR:
                nx,ny = r+dx,c+dy
                if inbound(nx,ny,row,col):
                    if ans[nx][ny] > ans[r][c]+1:
                        ans[nx][ny] = ans[r][c]+1
                        queue.append((nx,ny))
        return ans






