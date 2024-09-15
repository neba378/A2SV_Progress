class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        paths = set((a,b) for a,b in connections)
        visited = set()
        count = 0
        def rec(num):
            nonlocal count
            visited.add(num)
            for i in graph[num]:
                if i not in visited:
                    if (i,num) not in paths:
                        count+=1
                    rec(i)
        rec(0)
        return count

