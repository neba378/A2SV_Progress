class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s[:] == s[::-1]
        lst = []
        ans = []
        def bt(ind):
            nonlocal lst,ans
            if ind == len(s):
                ans.append(lst[:])
                return
            for i in range(ind,len(s)):
                if isPalindrome(s[ind:i+1]):
                    lst.append(s[ind:i+1])
                    bt(i+1)
                    lst.pop()
        bt(0)
        return ans



