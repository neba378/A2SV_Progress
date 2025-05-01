class Solution:
    def countAndSay(self, n: int) -> str:
        def runSum(s):
            i = 0
            j = 0
            lst = []
            while j<len(s):
                while j<len(s) and s[i] == s[j]:
                    j+=1
                lst.append(str(j-i) + s[i])
                i = j
            return ''.join(lst)
        
        count = 0
        s = '1'
        for i in range(n-1):
            s = runSum(s)
        return s
            

