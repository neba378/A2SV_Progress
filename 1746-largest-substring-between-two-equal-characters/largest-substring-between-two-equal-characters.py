class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        l,r = {},{}
        ans = -1
        for i in range(len(s)):
            if s[i] not in l:
                l[s[i]] = i
            r[s[i]] = i
        for ch in l:
            ans = max(ans,r[ch]-l[ch]-1)
        return ans