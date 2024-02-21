class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        one = 0
        two = 0
        ans = 0
        while target>2:
            if target%2!=0:
                one+=1
                target-=1
            if two>=maxDoubles:
                break
            target//=2
            two+=1
            
        if target>=2:
            ans+=(two+one+target-1)
        else:
            ans+=(one+two)
        return ans