class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = set(banned)
        ans = 0
        sum = 0
        for i in range(1,n+1):
            if i not in s:
                if i+sum<=maxSum:
                    sum+=i
                    ans+=1
                else:
                    break
        return ans