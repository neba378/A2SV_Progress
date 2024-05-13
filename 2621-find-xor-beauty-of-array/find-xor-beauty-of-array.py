class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            lst.append((i|i)&i)
        ans = 0
        for i in lst:
            ans^=i
        return ans