class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = []
        i = lo
        while i<hi+1:
            c = 0
            l = i
            while l!=1:
                if l%2 == 1:
                    l = 3*l+1
                else:
                    l = l//2
                c+=1
            ans.append((c,i))
            i+=1
        ans.sort()
        return ans[k-1][1]
