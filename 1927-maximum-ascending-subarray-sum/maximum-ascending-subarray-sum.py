class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        c = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i]< nums[i+1]:
                c+=nums[i]
            else:
                c+= nums[i]
                ans = max(ans,c)
                c = 0
            ans = max(ans,c)
            # print(c)
        if nums[i]< nums[i+1]:
            ans = max(ans,c+nums[i+1])
        return ans
