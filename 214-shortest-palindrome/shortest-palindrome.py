class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def isPalindrome(st):
            lst = [i for i in st]
            return lst == lst[::-1]
        j = len(s)-1
        while j>0:
            if s[j] == s[0] and isPalindrome(s[:j+1]):
                break
            j-=1
        t = s[j+1:]
        t = [i for i in t]
        t.reverse()
        t = "".join(t)
        ans = t+s
        return ans
