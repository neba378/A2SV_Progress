class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bN = []
        bit = [["0" for i in range(26)] for i in range(len(words))]
        for i in range(len(words)):
            for j in range(len(words[i])):
                bit[i][ord(words[i][j])-ord('a')] = "1"
            bN.append(int("".join(bit[i]),2))
        ans = 0
        for i in range(len(bN)):
            for j in range(i+1,len(bN)):
                if bN[i]&bN[j] == 0:
                    ans = max(ans,len(words[i]) * len(words[j]))
        return ans
                