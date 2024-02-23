class Solution:
    def sortSentence(self, s: str) -> str:
        lst = [_ for _ in s.split()]
        for i in lst:
            ''.join(sorted(i))
        lst.sort(key=lambda x: x[-1])
        st = ""
        for i in lst:
            st+=i[:len(i)-1]+" "
        
        return st[:len(st)-1]