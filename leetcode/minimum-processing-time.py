class Solution:
    def minProcessingTime(self, proT: List[int], t: List[int]) -> int:
        proT.sort()
        t.sort(reverse=True)
        j = 0
        ans = 0
        final = 0
        for i in proT:
            ans = max(i+t[j],i+t[(j+1)],i+t[(j+2)],i+t[(j+3)])
            j+=4
            final = max(final,ans)
        return final
