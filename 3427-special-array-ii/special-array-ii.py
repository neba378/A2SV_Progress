class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parity = [0]
        ans = []
        for i in range(len(nums)-1):
            if (nums[i]+nums[i+1])%2 == 1:
                parity.append(parity[-1]+1)
            else:
                parity.append(parity[-1]+0)
        for st,en in queries:
            if en-st == parity[en]-parity[st]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

