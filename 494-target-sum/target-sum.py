class Solution:
    def findTargetSumWays(self, nums: List[int], t: int) -> int:
        ans = 0
        n = len(nums)
        dic = {}
        def rec(n,s):
            nonlocal ans
            if s == t and n == len(nums):
                return 1
            if n == len(nums):
                return 0
            if (n,s) not in dic:
                dic[(n,s)] = rec(n+1,s+nums[n]) + rec(n+1,s-nums[n])
            return dic[(n,s)]
            
            
        return rec(0,0)
