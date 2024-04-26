class Solution:
    def checkIfPrerequisite(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        preReq = [0 for _ in range(n)]
        queue = deque()
        ans = [False for i in range(len(queries))]
        for f,t in edges:
            graph[f].append(t)
            preReq[t]+=1
        for i in range(len(preReq)):
            if preReq[i] == 0:
                queue.append(i)
        dic = defaultdict(set)
        while queue:
            node = queue.popleft()
            for ngh in graph[node]:
                preReq[ngh]-=1
                if dic[node]:
                    dic[ngh].update(dic[node])
                dic[ngh].add(node)
                
                if preReq[ngh] == 0:
                    queue.append(ngh)
        for i in range(len(queries)):
            queries[i].append(i)
        for uj,vj,j in queries:
            if uj in dic[vj]:
                ans[j] = True
        return ans