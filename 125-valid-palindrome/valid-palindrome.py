class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "abcdefghijklmnopqrstuvwxyz0123456789"
        s_lower = s.lower()
        lst = []
        for i in s_lower:
            if i in a:
                lst.append(i)
        lst_r = lst[:]
        lst_r.reverse()
        return lst_r == lst