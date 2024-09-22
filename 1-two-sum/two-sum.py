class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)):
            tag = target - nums[i]
            if tag in nums[i+1:]:
                lst.append(i)
                if nums[i] == tag:
                    nums[i] = -0.9
                    lst.append(nums.index(tag))
                else:
                    lst.append(nums.index(tag))
        return lst
