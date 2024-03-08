class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        best = left

        while left<=right:
            mid = (left+right)//2
            counter = 0
            t = 0
            for i in range(len(nums)):
                counter+=nums[i]
                if counter>mid:
                    counter = nums[i]
                    t+=1
            if t+1>k:
                left = mid+1
            else:
                best = mid
                right = mid-1
        return best
