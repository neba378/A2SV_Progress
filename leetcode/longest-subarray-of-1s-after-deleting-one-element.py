class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        count = 0
        cz = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                cz+=1
            while cz>1:
                if nums[i] == 0:
                    cz-=1
                i+=1          
            count = max(count,j-i)
        return count

