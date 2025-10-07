class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles >= numExchange:
            numBottles -= numExchange 
            numBottles+=1
            ans+=numExchange
        return ans+numBottles