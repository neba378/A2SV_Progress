class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        lst = [(i,j) for i,j in zip(efficiency,speed)]
        lst.sort(reverse=True)
        heap = []
        ans = 0
        sumSpeed = 0
        for e,s in lst:
            heappush(heap,s)
            sumSpeed+=s
            if len(heap)>k:
                sumSpeed-=heappop(heap)
            ans = max(ans,sumSpeed*e)
        return ans%(10**9+7)