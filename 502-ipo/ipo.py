class Solution:
    def findMaximizedCapital(self, k: int, w: int, p: List[int], c: List[int]) -> int:
        heap = []
        lst = [(c[i],p[i]) for i in range(len(p))]
        lst.sort()
        i = 0
        while i<len(p) and k>0:
            if lst[i][0]<=w:
                heappush(heap,-lst[i][1])
                i+=1
            else:
                if heap:
                    d = heappop(heap)
                    w-=d
                k-=1
        while k>0:
            if heap:
                w-=heappop(heap)
            k-=1
        return w


            
            
            