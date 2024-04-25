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
    def distanceLimitedPathsExist(self, n: int, ed: List[List[int]], q: List[List[int]]) -> List[bool]:
        uni = UnionFind(n)
        ans = [False for i in range(len(q))]
        for i in range(len(q)):
            q[i].append(i)
        q.sort(key = lambda x: x[2])
        ed.sort(key = lambda x:x[2])
        j = 0
        for i in q:
            while j<len(ed) and ed[j][2]<i[2]:
                uni.union(ed[j][0],ed[j][1])
                j+=1
            if uni.find(i[0]) == uni.find(i[1]):
                ans[i[3]] = True
        return ans
























