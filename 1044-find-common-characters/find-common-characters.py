class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lst = []
        l = len(words)
        for word in words:
            dic = defaultdict(int)
            for ch in word:
                dic[ch]+=1
            lst.append(dic)
        ans = []
        for word in words[0]:
            c = 0
            for j in range(1,len(words)):
                if lst[j][word]:
                    c+=1
                    lst[j][word]-=1
                else:
                    break
            if c == len(words)-1:
                ans.append(word)
        return ans