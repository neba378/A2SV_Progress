class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i,j = 0,0
        sumy = 0
        ans = 0
        s = set()
        while j<len(nums):
            if nums[j] not in s:
                s.add(nums[j])
                sumy+=nums[j]
                j+=1
            else:
                while nums[i] != nums[j]:
                    s.remove(nums[i])
                    sumy-=nums[i]
                    i+=1
                s.remove(nums[i])
                sumy-=nums[i]
                i+=1
            ans = max(ans,sumy)
        return ans