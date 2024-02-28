class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        count = 0
        cz = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                cz+=1
            while cz>k:
                if nums[i] == 0:
                    cz-=1
                i+=1          
            count = max(count,j-i+1)
        return count
