class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        col = [0]*len(graph)
        def bfs(i):
            if col[i]:
                return True
            queue = deque([i])
            col[i] = -1
            while queue:
                i = queue.pop()
                for neighbour in graph[i]:
                    if col[i] and col[neighbour] == col[i]:
                        return False
                    elif not col[neighbour]:
                        queue.append(neighbour)
                        col[neighbour] = -1*col[i]
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
            