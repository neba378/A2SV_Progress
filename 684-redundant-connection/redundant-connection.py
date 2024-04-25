# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(1,size+1)} # Using dictionary
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
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = UnionFind(len(edges))
        ans = []
        for edge in edges:
            i,j = edge[0],edge[1]
            if union.find(i) == union.find(j):
                ans.append(edge)
            union.union(i,j)
        return ans[-1]