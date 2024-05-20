class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target+1)]
        dp[0] =1
        nums.sort()
        for am in range(1,target+1):
            for i in nums:
                if am-i>=0:
                    dp[am]+=dp[am-i]
                else:
                    break
        return dp[target]