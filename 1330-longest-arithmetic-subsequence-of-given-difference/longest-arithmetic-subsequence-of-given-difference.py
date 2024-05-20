class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dic = {}
        ans = 0
        for i in arr:
            if i-diff in dic:
                dic[i] = dic[i-diff]+1
            else:
                dic[i] = 1
            ans = max(ans,dic[i])
        return ans

