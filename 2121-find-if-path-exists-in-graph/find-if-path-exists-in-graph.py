class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        def rec(start,dest,visited):
            if start == dest:
                return True
            visited.add(start)
            for i in graph[start]:
                print()
                if i not in visited:
                    found = rec(i,dest,visited)
                    if found:
                        return True
            return False
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        print(graph)
        return rec(source,destination,visited)
                    
        