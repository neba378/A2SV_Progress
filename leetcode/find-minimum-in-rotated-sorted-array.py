class Solution:
    def findMin(self, n: List[int]) -> int:
        i,j = 0, len(n)-1
        while i<=j:
            mid = (i+j)//2

            if n[j]<n[i]:
                if n[mid]>n[j]:
                    i = mid+1
                else:
                    j = mid
            else:
                break
        return n[i]