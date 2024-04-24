class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        heap = []
        i = 0
        c = 0
        ans = []
        while i<len(tasks) or heap:
            if not heap:
                c = max(c,tasks[i][0])
            while i<len(tasks) and c>=tasks[i][0]:
                et,pt,ind = tasks[i]
                heappush(heap,(pt,ind))
                i+=1
            if heap:
                hp = heappop(heap)                    
                c+=hp[0]
                ans.append(hp[1])
        return ans

