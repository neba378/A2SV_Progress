class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row,col = len(maze),len(maze[0])
        def isValid(x,y):
            return 0<=x<row and 0<=y<col
        DIR = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque([[(entrance[0],entrance[1])]])
        # print(queue)
        visited = set()
        count = 0
        while queue:
            point = (queue.popleft())
            # print(point)
            lst = []
            count+=1
            for i in range(len(point)):
                visited.add(point[i])
                # print(point[i])
                x,y = point[i]
                for dx,dy in DIR:
                    # print("mn",x+dx,y+dy)
                    if (x+dx,y+dy) not in visited and isValid(x+dx,y+dy) and maze[x+dx][y+dy] == "." and (x+dx == row-1 or y+dy == col-1 or x+dx == 0 or y+dy == 0):
                        return count
                    if isValid(x+dx,y+dy) and (x+dx,y+dy) not in visited and maze[x+dx][y+dy] == ".":
                        visited.add((x+dx,y+dy))
                        lst.append((x+dx,y+dy))
            if lst != []:
                queue.append(lst)
        return -1