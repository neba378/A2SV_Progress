class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for pack in times:
            graph[pack[0]].append([pack[1],pack[2]])
        processed = set()
        distance = {i:float("inf") for i in range(1,n+1)}
        if k not in graph:return -1 
        distance[k] = 0
        heap = [k]
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap)
            if node in processed:
                continue
            for ch,wg in graph[node]:
                dist = distance[node]+wg
                if dist<distance[ch]:
                    distance[ch] = dist
                    heapq.heappush(heap,ch)
        m=max(distance.values())

        return m if m!=float('inf') else -1
