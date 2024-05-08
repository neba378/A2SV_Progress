class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            lowerBit = 0
            upperBit = 0
            for j in range(i,n):
                if s[j].islower():
                    lowerBit = lowerBit|(1<<(ord(s[j])-ord("a")))
                elif s[j].isupper():
                    upperBit = upperBit|(1<<(ord(s[j])-ord("A")))
                if lowerBit == upperBit and len(ans)<j-i+1:
                    ans = s[i:j+1]
        return ans
