class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        diff = 0
        for i in range(len(prices)):
            mini = min(mini,prices[i])
            diff = max(diff,prices[i]-mini)
        return diff