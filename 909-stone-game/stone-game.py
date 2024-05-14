class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(l,r,t):
            if l>r:
                return 0
            if (l,r,t) not in memo:
                if t:
                    a = piles[l]+dp(l+1,r,0)
                    b = piles[r]+dp(l,r-1,0)
                    memo[(l,r,t)] = max(a,b)
                else:
                    a = piles[l]+dp(l+1,r,1)
                    b = piles[r]+dp(l,r-1,1)
                    memo[(l,r,t)] = min(a,b)
            return memo[(l,r,t)]
        return True if dp(0,len(piles)-1,1)>0 else False