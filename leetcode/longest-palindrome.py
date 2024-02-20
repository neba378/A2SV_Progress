class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        count = 0
        check = False
        for i,j in counter.items():
            if j%2 == 0:
                count+=j
            else:
                count+=j-1
                check = True
        if check:
            return count+1
        return count