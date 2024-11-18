class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1,l2 = len(num1),len(num2)
        ans = []
        c = 0
        i,j = l1-1,l2-1
        while i>=0 and j>=0:
            s = int(num1[i])+int(num2[j])+c
            c = s//10
            ans.append(str(s%10))
            i-=1
            j-=1
        if i>=0:
            while i>=0:
                s = int(num1[i])+c
                c = s//10
                ans.append(str(s%10))
                i-=1
        elif j>=0:
            while j>=0:
                s = int(num2[j])+c
                c = s//10
                ans.append(str(s%10))
                j-=1
        if c!=0:
            ans.append(str(c))
        ans.reverse()
        # print(ans)
        return "".join(ans)
