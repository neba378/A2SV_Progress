# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)} # Using dictionary
        # self.parent = [i for i in range(size)] # Using list
        self.rank = defaultdict(int)
        
    def find(self, x):
        
        while(x != self.parent[x]):
            x = self.parent[x]
        return x
		
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if py!=px:
            if self.rank[py]>self.rank[px]:
                self.parent[px] = py
            elif self.rank[py]<self.rank[px]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px]+=1
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhatDist(po1,po2):
            return abs(po1[0]-po2[0])+abs(po1[1]-po2[1])
        uni = UnionFind(len(points))
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                d = manhatDist(points[i],points[j])
                edges.append((d,i,j))
        edges.sort()
        ans = 0
        num_edges_connected = 0
        for d,i,j in edges:
            if not uni.connected(i,j):
                uni.union(i,j)
                ans+=d
                num_edges_connected+=1
            if num_edges_connected == len(points)-1:
                break
        return ans

        
