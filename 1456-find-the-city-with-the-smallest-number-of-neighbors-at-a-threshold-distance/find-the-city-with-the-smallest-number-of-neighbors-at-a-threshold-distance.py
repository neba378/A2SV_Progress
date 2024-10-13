class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for i in range(n)]
        for i,j,w in edges:
            dist[i][j] = dist[j][i] = w
        for i in range(n):
            dist[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
        lst = [0]*n
        for i in range(n):
            for j in range(n):
                if dist[i][j]<=distanceThreshold:
                    lst[i]+=1
        # print(lst)
        ans = -1
        val = float("inf")
        for i in range(len(lst)):
            if val>=lst[i]:
                val = lst[i]
                ans = i
        return ans

