class Solution:
    def search(self, n: List[int], target: int) -> int:
        i = 0
        j = len(n)-1
        while i<=j:
            mid = (i+j)//2
            if target == n[mid]:
                return mid
            elif target>n[mid]:
                i = mid+1
            else:
                j = mid-1
        return -1