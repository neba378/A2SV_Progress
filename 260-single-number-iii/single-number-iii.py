class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] ^ nums[j] == 0:
                    seen.add(nums[i])
                    break
            if nums[i] not in seen:
                ans.append(nums[i])
        return ans
