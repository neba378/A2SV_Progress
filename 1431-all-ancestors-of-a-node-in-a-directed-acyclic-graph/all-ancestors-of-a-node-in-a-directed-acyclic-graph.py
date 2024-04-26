



class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        preReq = [0 for _ in range(n)]
        queue = deque()
        ans = []

        for f,t in edges:
            graph[f].append(t)
            preReq[t]+=1
        for i in range(len(preReq)):
            if preReq[i] == 0:
                queue.append(i)
        print(queue)
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
        ans = []
        for i in range(n):
            ans.append(sorted(list(dic[i])))
        return ans