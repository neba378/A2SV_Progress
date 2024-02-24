class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j = 0,0
        if len(name)>len(typed):
            return False;
        while j<len(typed):
            if i<len(name) and name[i] == typed[j]:
                while i<len(name) and j<len(typed) and  name[i] == typed[j]:
                    i+=1
                    j+=1
                if i!=0:
                    while j<len(typed) and name[i-1] == typed[j]:
                        j+=1
            else:
                return False
        return i==len(name)