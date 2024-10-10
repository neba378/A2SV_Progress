class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float("inf")]*n
        prev[src] = 0
        graph = defaultdict(list)
        for pack in flights:
            graph[pack[0]].append((pack[1],pack[2]))
        lst = deque([src])
        
        for i in range(k+1):
            cur = prev[:]
            temp = set()
            for j in lst:
                for v,p in graph[j]:
                    cur[v] = min(cur[v],prev[j]+p)
                    temp.add(v)
            lst = deque(temp)
            
            prev =  cur
        
        return cur[dst] if cur[dst]!=float('inf') else -1