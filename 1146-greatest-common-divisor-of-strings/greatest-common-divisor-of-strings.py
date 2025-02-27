class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        dic = {}
        maxL = max(l1,l2)
        minL = min(l1,l2)

        for i in range(minL):
            if str1[i]!=str2[i]:
                return ""
            if not (maxL%(i+1)) and not (minL%(i+1)):
                dic[str1[:i+1]] = maxL//(i+1)
        big = str1 if l1>=l2 else str2
        ans = ""
        for k,v in dic.items():
            if k*v == big and len(k)>len(ans):
                ans = k
        return ans
