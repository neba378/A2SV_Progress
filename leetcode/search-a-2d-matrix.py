class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        row = len(m)
        col = len(m[0])
        i,j = 0, row*col-1
        while i<=j:
            mid = i+ (j-i)//2
            if m[mid//col][mid%col]<t:
                i = mid+1
            elif m[mid//col][mid%col]>t:
                j = mid-1
            else:
                return True
        return False


            
