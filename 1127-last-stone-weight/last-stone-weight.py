class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = 0-stones[i]
        while len(stones)>1:
            heapify(stones)
            a = heappop(stones)
            b = heappop(stones)
            a = -1*a
            b = -1*b
            heappush(stones,-1*(a-b))
        return abs(stones[0])
        


