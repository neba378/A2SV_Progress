class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums)-1
        count = 0
        nums.sort()

        while(j>i):
            if nums[i]+nums[j]==k:
                count+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]>k:
                j-=1
            else:
                i+=1
        return count