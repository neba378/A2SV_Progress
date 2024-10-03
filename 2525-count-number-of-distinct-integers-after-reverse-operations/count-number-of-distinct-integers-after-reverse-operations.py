class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(n):
            lst = [i for i in str(n)]
            return int("".join(reversed(lst)))
        ans = 0
        for i in range(len(nums)):
            nums.append(reverse(nums[i]))
        return len(set(nums))

