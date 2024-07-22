class Solution:
    
    def longestCycle(self, edges: List[int]) -> int:
        self.ans = -1
        visited = set()
        def dfs(v,dist):
            ngh = edges[v]
            visited.add(v)
            if ngh!=-1 and ngh not in visited:
                dist[ngh] = dist[v]+1
                dfs(ngh,dist)
            elif ngh!=-1 and ngh in dist:
                self.ans = max(self.ans,dist[v]-dist[ngh]+1)
        for i in range(len(edges)):
            if i not in visited:
                dist = {i:1}
                dfs(i,dist)
        return self.ans

