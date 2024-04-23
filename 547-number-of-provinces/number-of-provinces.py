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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uni = UnionFind(len(isConnected))
        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if isConnected[r][c] == 1:
                    uni.union(r,c)
        vis = set()     
        for i in range(len(isConnected)):
            vis.add(uni.find(i))
        return len(vis)
         