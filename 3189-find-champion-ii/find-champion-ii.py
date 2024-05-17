class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        pre = defaultdict(int)
        for i in range(n):
            pre[i]=0
        for u,v in edges:
            pre[v]+=1
        ans = []
        c = 0
        for i,j in pre.items():
            if j == 0:
                v = i
                c+=1
            if c>1:
                return -1
        if c==0:
            return -1
        return v