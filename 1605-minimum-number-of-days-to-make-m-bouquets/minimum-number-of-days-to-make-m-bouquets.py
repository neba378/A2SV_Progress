class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(lst):
            c = 0
            ans = 0
            for i in range(len(lst)):
                if lst[i] <= 0:
                    c+=1
                    if c == k:
                        ans+=1
                        c = 0
                else:
                    c = 0
            return ans
        if len(bloomDay)<m*k:
            return -1
        left,right = min(bloomDay),max(bloomDay)
        mid = (left+right)//2
        while left<=right:
            mid = left + (right-left)//2
            temp = bloomDay[:]
            for i in range(len(temp)):
                temp[i]-=mid
            t = check(temp)
            if left == right:
                return left
            elif t>=m:
                right = mid
            else:
                left = mid+1
        return mid
            
