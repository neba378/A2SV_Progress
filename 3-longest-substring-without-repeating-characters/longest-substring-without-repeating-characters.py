class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        dic = defaultdict(int)
        ans = 0
        for j in range(len(s)):
            if dic[s[j]] == 1:
                while i<j:
                    if s[i] == s[j]:
                        dic[s[i]]-=1
                        i+=1
                        break
                    dic[s[i]]-=1
                    i+=1
                    
            dic[s[j]]+=1
            ans = max(ans,j-i+1)
        return ans

