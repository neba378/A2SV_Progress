class Solution:
    def hIndex(self, c: List[int]) -> int:
        i = 0
        j = len(c)-1
        while i<=j:
            mid = (i+j)//2
            if len(c)-mid == c[mid]:
                return len(c)-mid
            elif len(c)-mid>c[mid]:
                i = mid+1
            else:
                j =  mid-1
        return len(c)-i