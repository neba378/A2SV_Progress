class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        Tco = nums.count(1)
        Tcz = nums.count(0)
        col = 0
        cr = 0
        cz = 0
        lst = [Tco]
        for i in range(len(nums)):
            if nums[i] == 0:
                cz+=1
            if nums[i] == 1:
                col+=1
            cr = Tco-col
            lst.append(cr+cz)
        maxi = max(lst)
        ans = []
        for i in range(len(lst)):
            if lst[i]==maxi:
                ans.append(i)
        return ans