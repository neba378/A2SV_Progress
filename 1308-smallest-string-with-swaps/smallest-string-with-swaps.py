# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}  # Using dictionary
        # self.parent = [i for i in range(size)] # Using list
        self.rank = defaultdict(int)
        self.mini = {i: i for i in range(size)}

    def find(self, x):

        while (x != self.parent[x]):
            x = self.parent[x]
        return x

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if py != px:
            if self.rank[py] > self.rank[px]:
                self.parent[px] = py
            elif self.rank[py] < self.rank[px]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uni = UnionFind(len(s))
        for i in pairs:
            uni.union(i[0],i[1])
        dic = defaultdict(list)
        for i in range(len(s)):
            dic[uni.find(i)].append(s[i])
        ans = []
        print(dic)
        for i in dic:
            dic[i].sort(reverse=True)
        for i in range(len(s)):
            group = dic[uni.find(i)]
            ans.append(group.pop())
        return "".join(ans)
