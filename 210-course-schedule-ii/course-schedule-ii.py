class Solution:
    def findOrder(self, c: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(c)]
        preReq = [0 for _ in range(c)]
        queue = deque()
        ans = []

        for course,pre in prerequisites:
            graph[pre].append(course)
            preReq[course]+=1
        for i in range(len(preReq)):
            if preReq[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            ans.append(node)
            for ngh in graph[node]:
                preReq[ngh]-=1

                if preReq[ngh] == 0:
                    queue.append(ngh)
        return [] if len(ans)<c else ans


            
