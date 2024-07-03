class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        def dif(lst):
            a = []
            lst.sort()
            for i in range(1,len(lst)):
                a.append(lst[i]-lst[i-1])
            return a
        for i in range(len(l)):
            lst = dif(nums[l[i]:r[i]+1])
            ans.append(len(set(lst)) == 1)
        return ans