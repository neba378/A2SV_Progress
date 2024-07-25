class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        ans,s = 0,0
        while s<target or (s-target)%2!=0:
            ans+=1
            s+=ans
        return ans