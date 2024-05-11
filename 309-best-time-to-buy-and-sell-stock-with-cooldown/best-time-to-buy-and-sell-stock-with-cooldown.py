class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [0]*n
        sell = [0]*n
        cool = [0]*n
        buy[0] = -prices[0]
        sell[0] = 0
        cool[0] = 0

        for i in range(1,n):
            buy[i] = max(buy[i-1],cool[i-1]-prices[i])
            sell[i] = max(buy[i-1]+prices[i],sell[i-1])
            cool[i] = max(cool[i-1],sell[i-1])
        return max(sell[n-1],cool[n-1])


       