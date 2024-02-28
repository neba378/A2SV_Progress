class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = 0
        if len(nums) == 1:
            return True
        for i,j in enumerate(nums[0:len(nums)-1]):
            maxi = max(maxi, (i+j))
            if maxi >= len(nums)-1:
                return True
            if maxi<i+1:
                return False
        return False
                