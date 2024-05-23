class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == len(needle):
            j = 0
            for i in range(len(haystack)):
                if haystack[i] != needle[i]:
                    return -1
                else:
                    j+=1
            if j == len(haystack):
                return 0
                
        for i in range(len(haystack)-len(needle)+1):
            k = i
            for j in range(len(needle)):
                if haystack[k] == needle[j]:
                    k = k +1
                    if j == len(needle)-1:
                        return  i
                else:
                    break
        return -1