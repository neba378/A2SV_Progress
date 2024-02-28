import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = 1
        left = 1
        l = [1]*len(nums)
        r = [1]*len(nums)
        p = [1]*len(nums)
        for i in range(1,len(nums)):
            l[i] = l[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            r[j] = r[j+1] * nums[j+1]
        for i in range(len(nums)):
            p[i] = l[i]*r[i]
        return p
