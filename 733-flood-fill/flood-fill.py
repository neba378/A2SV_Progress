class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        graph = defaultdict(list)
        for r in range(len(image)):
            for c in range(len(image[0])):
                if image[r][c] == image[sr][sc]:
                    if r-1>=0:
                        if image[r-1][c] == image[sr][sc]:
                            graph[(r,c)].append((r-1,c))
                    if c-1>=0:
                        if image[r][c-1] == image[sr][sc]:
                            graph[(r,c)].append((r,c-1))
                    if c+1<len(image[0]):
                        if image[r][c+1] == image[sr][sc]:
                            graph[(r,c)].append((r,c+1))
                    if r+1<len(image):
                        if image[r+1][c] == image[sr][sc]:
                            graph[(r,c)].append((r+1,c))
        visited = set()
        def dfs(graph,sr,sc,color,image):
            visited.add((sr,sc))
            image[sr][sc] = color
            for i in graph[(sr,sc)]:
                if i not in visited:
                    dfs(graph,i[0],i[1],color,image)
        dfs(graph,sr,sc,color,image)
        return image