class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        def sqrt(n):
            return int((-n)**(1/2))
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)
        for i in range(k):
            num = heapq.heappop(gifts)
            heapq.heappush(gifts,-sqrt(num))
        return -sum(gifts)