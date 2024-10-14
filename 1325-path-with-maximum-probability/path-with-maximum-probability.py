class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1],succProb[i]])
            graph[edges[i][1]].append([edges[i][0],succProb[i]])
        prob = [0 for i in range(n)]
        processed = set()
        prob[start_node] = 1
        heap = [(-1,start_node)]
        while heap:
            pr,node = heapq.heappop(heap)
            if node in processed:
                continue
            processed.add(node)
            for ngh, pro in graph[node]:
                probability = pr*pro
                if probability<prob[ngh]:
                    prob[ngh] = probability
                    heapq.heappush(heap,(probability,ngh))
        return -prob[end_node]