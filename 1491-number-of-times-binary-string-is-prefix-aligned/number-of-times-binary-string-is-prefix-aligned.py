class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        l = 0
        maxi = 0
        ans = 0
        for i in range(len(flips)):
            if maxi<flips[i]:
                maxi = flips[i]
            l+=1

            if l == maxi:
                ans+=1
        return ans

