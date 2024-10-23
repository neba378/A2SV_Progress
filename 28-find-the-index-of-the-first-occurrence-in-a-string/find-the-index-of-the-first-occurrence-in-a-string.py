class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            ind = i
            j = 0
            while j<len(needle):
                if ind<len(haystack) and haystack[ind] == needle[j]:
                    ind+=1
                else:
                    break
                j+=1
            if j == len(needle):
                return i
        return -1
                
