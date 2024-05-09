class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dic = {}
        def rec(s,ind):
            if ind>=len(nums):
                return False
            if s == 0:
                return True
            if s<0:
                return False
            state = (s,ind)

            if state not in dic:
                dic[state] = rec(s-nums[ind],ind+1)or rec(s,ind+1)
            return dic[state]
        tot = sum(nums)
        if tot%2 == 1:
            return False
        return rec(tot//2,0)