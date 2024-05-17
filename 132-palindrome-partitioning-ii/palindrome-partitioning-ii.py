class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(s):
            return s[:] == s[::-1]
        min_cuts = float('inf')
        memo = {}
        def bt(ind):
            nonlocal min_cuts
            if ind == len(s):
                return 0
            if ind not in memo:
                for i in range(ind,len(s)):
                    if isPalindrome(s[ind:i+1]):
                        min_cuts = min(min_cuts,1+bt(i+1))
                memo[ind] = min_cuts
            return memo[ind]
        
        return bt(0)-1