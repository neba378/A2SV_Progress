class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inbound(r,c,row,col):
            return 0<=r<row and 0<=c<col
        DIR = [(1,0),(0,1),(-1,0),(0,-1)]
        graph = defaultdict(list)
        row,col = len(board),len(board[0])
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    for dr,dc in DIR:
                        nr,nc = r+dr,c+dc
                        if inbound(nr,nc,row,col) and board[nr][nc] == "O":
                            graph[(r,c)].append((nr,nc))
        unique = set()
        lst = set()
        def dfs(r,c):
            unique.add((r,c))
            for nb in graph[(r,c)]:
                if ((nb[0],nb[1])) not in unique:
                    dfs(nb[0],nb[1])
        for i in range(col):
            if board[0][i] == "O":
                lst.add((0,i))
            if board[row-1][i] == "O":
                lst.add((row-1,i))
        for i in range(row):
            if board[i][0] == "O":
                lst.add((i,0))
            if board[i][col-1] == "O":
                lst.add((i,col-1))
        for i in lst:
            dfs(i[0],i[1])
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r,c) not in unique:
                    board[r][c] = "X"
        



