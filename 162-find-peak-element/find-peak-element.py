class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums = [float('-inf')]+nums+[float('-inf')]
        n = len(nums)
        i,j = 1,n-1
        while i<j:
            mid = (i+j)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid-1
            elif nums[mid]<nums[mid+1]:
                i = mid+1
            else:
                j = mid
        return -1
