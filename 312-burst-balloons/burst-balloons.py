class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        nums = [1]+nums+[1]

        def rec(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            for i in range(l,r+1):
                c = nums[i]*nums[l-1]*nums[r+1]
                l_p = rec(l,i-1)
                r_p = rec(i+1,r)
                dp[(l,r)] = max(dp[(l,r)],c+l_p+r_p)
            return dp[(l,r)]
        return(rec(1,len(nums)-2))