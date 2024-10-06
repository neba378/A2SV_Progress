class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startBin = bin(start)[2:]
        goalBin = bin(goal)[2:]
        maxi = max(len(startBin),len(goalBin))
        goalFullBin = (maxi-len(goalBin))*"0"+goalBin
        startFullBin = (maxi-len(startBin))*"0"+ startBin
        ans = 0
        for i in range(len(startFullBin)):
            if goalFullBin[i]!=startFullBin[i]:
                ans+=1
        return ans
