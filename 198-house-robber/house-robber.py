class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==2:
            return nums[0] if nums[0]>nums[1] else nums[1]
        elif len(nums) == 1:
            return nums[0]
        nums[-3]+=nums[-1]
        for i in range(len(nums)-4,-1,-1):
            nums[i]+=nums[i+2] if nums[i+2]>nums[i+3] else nums[i+3]
        return nums[0] if nums[0]>nums[1] else nums[1]