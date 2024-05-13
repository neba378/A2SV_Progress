class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo = {}
        # def dp(ind,prev):
        #     if ind == len(nums):
        #         return 0
        #     if (ind,prev) not in memo:
        #         inc = 0
        #         if prev == -1 or nums[ind]>nums[prev]:
        #             inc = 1+dp(ind+1,ind)
        #         exc = dp(ind+1,prev)
        #         memo[(ind,prev)] = max(inc,exc)
        #     return memo[(ind,prev)]
        # return dp(0,-1)

        dic = defaultdict(int)
        maxi = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            maxRep = 0
            maxi = max(maxi,nums[i])
            
            for j in range(nums[i]+1,maxi+1):
                maxRep = max(maxRep,dic[j])
            dic[nums[i]] = max(1+maxRep,dic[nums[i]])
            
        return max(dic.values())

        