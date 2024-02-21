class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = [nums[0]]
        for i in range(1,len(nums)):
            lst.append(lst[-1]+nums[i])
        return lst