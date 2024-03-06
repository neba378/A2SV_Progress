class Solution:
    def findRadius(self, ho: List[int], he: List[int]) -> int:
        def check(mid,ho,he):
            i,j = 0 ,0
            while i<len(ho) and j<len(he):
                while j<len(he) and abs(he[j]-ho[i])>mid:
                    j+=1
                else:
                    i+=1
            if j == len(he):
                return False
            return True
        left, right = 0, max(max(ho),max(he))
        ho.sort()
        he.sort()
        while left<right:
            mid = left + (right-left)//2
            if check(mid,ho,he):
                right = mid
            else:
                left = mid+1
        return left
        
