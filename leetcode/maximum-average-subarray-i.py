class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i,j = 0,k
        tot = sum(nums[0:k])
        ans = tot
        for _ in range(len(nums)-k):
            tot+=nums[_+k]-nums[_]
            ans = max(tot,ans)
        return ans/k
            