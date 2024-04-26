class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe_type = {}
        def dfs(i):
            if i in safe_type:
                return safe_type[i]
            safe_type[i] = False
            for ngh in graph[i]:
                if not dfs(ngh):
                    return False
            safe_type[i] = True
            return safe_type[i]
        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans