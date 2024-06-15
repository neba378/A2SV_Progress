class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        ans = []
        for i in nums:
            if i<0:
                neg.append(i**2)
            else:
                pos.append(i**2)
        i = 0
        j = len(neg)-1
        while j>=0 and i<len(pos):
            if pos[i]>neg[j]:
                ans.append(neg[j])
                j-=1
            else:
                ans.append(pos[i])
                i+=1
        
        ans.extend(pos[i:])
        while j>=0:
            ans.append(neg[j])
            j-=1
        return ans

