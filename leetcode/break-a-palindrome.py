class Solution:
    def breakPalindrome(self, s: str) -> str:
        f = True
        p = []
        for i in s:
            p.append(i)
        if len(p) == 1:
            return ""
        for i in range(len(p)):
            if p[i] == 'a':
                continue
            else:
                f =False
                if i<len(p)-1 and i>0:
                    if p[i-1] == 'a' and p[i+1]  == 'a':
                        while i+1<len(p) and p[i+1] == 'a':
                            i+=1
                        p[i] = 'b'
                        break
                p[i] = 'a'
                break
        if f:
            p[-1] = 'b'
            return "".join(p)
            
        else:
            return "".join(p)