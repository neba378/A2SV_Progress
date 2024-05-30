class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        c = len(quiet)
        graph = [[] for _ in range(c)]
        preReq = [0 for _ in range(c)]
        queue = deque()
        ans = []
        dic = {}
        for i,q in enumerate(quiet):
            dic[q] = i
        for rich,poor in richer:
            graph[rich].append(poor)
            preReq[poor]+=1
        for i in range(c):
            if preReq[i] == 0:
                queue.append(i)
        ansi = [quiet[_] for _ in range(c)]
        while queue:
            node = queue.popleft()
            # ans.append(node)
            for ngh in graph[node]:
                preReq[ngh]-=1
                # print("ngh",ngh,"node",node,min(ansi[ngh],ansi[node]))
                ansi[ngh] = min(ansi[ngh],ansi[node])
                if preReq[ngh] == 0:
                    queue.append(ngh)
        for answer in ansi:
            ans.append(dic[answer])
        return ans