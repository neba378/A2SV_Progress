class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        maxi = 1
        mini = 1
        for num in nums:
            mult = maxi*num
            maxi = max(mult,num,mini*num)
            mini = min(mult,num,mini*num)
            ans = max(ans,maxi)
        return ans
