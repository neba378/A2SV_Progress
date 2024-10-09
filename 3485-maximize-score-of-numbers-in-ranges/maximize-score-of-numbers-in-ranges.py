class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        right = start[-1]+d+1
        left = 0
        while left<right:
            mid = left+(right-left)//2
            pre = start[0]
            f = True
            for i in range(1,len(start)):
                if start[i]-pre + d < mid:
                    f = False
                    break
                pre = max(start[i],pre+mid)
            if f:
                left = mid+1
            else:
                right = mid
        return left-1
            


