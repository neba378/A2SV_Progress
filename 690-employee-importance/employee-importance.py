"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = defaultdict(list)
        for i in employees:
            dic[i.id].append(i.importance)
            dic[i.id].extend(i.subordinates)
        ans = 0
        def bfs(graph, start):
            nonlocal ans
            visited = set()
            queue = deque([start])
            visited.add(start)
            
            while queue:
                node = queue.popleft()
                ans+=dic[node][0]

                for neighbor in graph[node][1:]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        bfs(dic,id)
        return ans