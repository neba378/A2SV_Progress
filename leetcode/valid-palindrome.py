class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(filter(str.isalnum, s)).lower()
        le = len(s1)
        for i, j in zip(range(0,le//2+1), range(le-1,le//2-1,-1)):
            if s1[i] != s1[j]:
                return False
        return True