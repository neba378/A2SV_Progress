class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            dic = {}
            dic2 = {}
            f = True
            for i in range(len(word)):
                if word[i] in dic:
                    if dic[word[i]]!=pattern[i]:
                        f = False
                        break
                    else:
                        continue
                elif pattern[i] in dic2:
                    if dic2[pattern[i]]!=word[i]:
                        f = False
                        break
                    else:
                        continue
                else:
                    dic[word[i]] = pattern[i]
                    dic2[pattern[i]] = word[i]
            if f:
                ans.append(word)
        return ans
