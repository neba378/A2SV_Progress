class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        pre = defaultdict(int)
        for i in range(n):
            pre[i]=0
        for u,v in edges:
            pre[v]+=1
            pre[u] = max(pre[u],0)
        ans = []
        for i,j in pre.items():
            if j == 0:
                ans.append(i)
        if len(ans)>1 or len(ans)==0:
            return -1
        return ans[0]