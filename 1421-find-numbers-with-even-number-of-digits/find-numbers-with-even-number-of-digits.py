class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def countEven(num):
            return len(str(num))
        ans = 0
        for i in nums:
            if not countEven(i)%2:
                ans+=1
        return ans