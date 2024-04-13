class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def cellToAdd(cell):
            row = (cell-1)//n
            col = (cell-1)%n
            if row%2 == 1:
                col = n-1-col
            return (row,col)
        queue = deque([(1,0)])
        visited = set()
        while queue:
            cell,dist = queue.popleft()
            for i in range(1,7):
                new_cell = cell+i
                row,col = cellToAdd(new_cell)
                if board[row][col] != -1:
                    new_cell = board[row][col]
                if new_cell == n*n:
                    return dist+1
                if (row,col) not in visited:
                    queue.append((new_cell,dist+1))
                    visited.add((row,col))
        return -1