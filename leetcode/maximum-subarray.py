class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## kandane's Algorithm
        curr = nums[0]
        maximum = -10001
        maximum = max(curr,maximum)
        for i in range(1,len(nums)):
            curr = max(curr,0)
            curr+=nums[i]
            maximum = max(curr,maximum)
        return maximum
        