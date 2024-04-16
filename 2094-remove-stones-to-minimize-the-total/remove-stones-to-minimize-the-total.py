class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for j in range(len(piles)):
            piles[j] = piles[j]*-1

        heapify(piles)
        
        for i in range(k):
            val = heappop(piles)
            val *=-1
            fl = val//2
            val -=fl
            heappush(piles,-1*val)
        return -1*sum(piles)

