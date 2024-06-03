class Solution:
    def appendCharacters(self, t: str, s: str) -> int:
        left = right = 0 
        while left < len(s) and right < len(t):
            if s[left] == t[right]: 
                left += 1
            right += 1
        return len(s)-left
        