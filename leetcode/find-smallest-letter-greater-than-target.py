class Solution:
    def nextGreatestLetter(self, l: List[str], target: str) -> str:
        i = 0
        j = len(l)-1
        while i<=j:
            mid = (i+j)//2
            if target >= l[mid]:
                i = mid+1
            else:
                j = mid-1
        if j == -1:
            return l[0]
        else:
            return l[i%len(l)]