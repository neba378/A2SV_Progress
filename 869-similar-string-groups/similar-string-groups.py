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
    def numSimilarGroups(self, strs: List[str]) -> int:
        def check(s,t):
            c=0
            if Counter(s)!=Counter(t):
                return False
            for i in range(len(s)):
                if s[i]!=t[i]:
                    if c == 2:
                        return False
                    c+=1
            return True
        uni = UnionFind(len(strs))
        for i in range(len(strs)):
            for j in range(len(strs)):
                if check(strs[i],strs[j]):
                    uni.union(i,j)
        s = set()
        for i in range(len(strs)):
            s.add(uni.find(i))
       
        return len(s)