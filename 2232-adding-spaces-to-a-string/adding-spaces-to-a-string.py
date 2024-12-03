class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        i = 0
        for j in range(len(s)):
            if i<len(spaces) and j == spaces[i]:
                ans.append(" ")
                i+=1
            ans.append(s[j])
        return "".join(ans)