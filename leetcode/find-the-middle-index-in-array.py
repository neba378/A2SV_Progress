class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lst = [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            lst.append(lst[-1]+nums[i])
        prefix_sum = list(accumulate(nums))
        lst.reverse()
        for i in range(len(lst)):
            if lst[i] == prefix_sum[i]:
                return i
        return -1
