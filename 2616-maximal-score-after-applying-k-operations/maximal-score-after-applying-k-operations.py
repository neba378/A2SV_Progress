class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        ans = 0
        for i in range(k):
            popped = heapq.heappop(heap)
            ans-=popped
            ceiled = math.ceil(-popped/3)
            heapq.heappush(heap,-ceiled)
        return ans