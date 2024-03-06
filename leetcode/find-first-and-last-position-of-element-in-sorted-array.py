class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = bisect_left(nums,target)
        y = bisect_right(nums,target)
        if x == y and len(nums)!=1:
            return [-1,-1]
        if len(nums) == 1 and nums[0]!=target:
            return [-1,-1]
        return [x,y-1]