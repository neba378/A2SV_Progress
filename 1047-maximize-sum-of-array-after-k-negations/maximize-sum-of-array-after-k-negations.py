class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0

        while i<len(nums) and k>0:
            if nums[i]<0:
                nums[i] = -nums[i]
                i+=1
            else:
                break
            k-=1
        nums.sort()
        if k>0:
            if k%2:
                nums[0] = -nums[0]
        
        return sum(nums)
        