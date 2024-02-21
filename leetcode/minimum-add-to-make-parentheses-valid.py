class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        dic = {"(":0, ")":0}
        for i in s:
            if i == ")":
                if dic["("]>0:
                    dic["("]-=1
                else:
                    dic[")"]+=1
            else:
                dic["("]+=1
        return dic["("]+dic[")"]