class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2)>len(str1):
            return False
        i,j = 0,0
        while j<len(str2) and i<len(str1):
            x,y = ord(str1[i]),ord(str2[j])
            if x == y or ((x-ord("a")+1)%26 == (y-ord('a'))):
                j+=1
            i+=1
        return j>=len(str2)