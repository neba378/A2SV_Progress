class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        distinct = list(set(nums))
        distinct.sort()
        lenNums = len(nums)
        lenDistinct = len(distinct)
        for i in range(lenDistinct):
            nums[i]=distinct[i]
        for i in range(lenDistinct,lenNums):
            nums[i] = "_"
        return lenDistinct