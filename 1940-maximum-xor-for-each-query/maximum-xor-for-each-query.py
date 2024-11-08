class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        c = 0
        
        ans = []
        for i in range(len(nums)):
            c ^= nums[i]
            ans.append((2**maximumBit-1)^c)
        ans.reverse()
        return ans