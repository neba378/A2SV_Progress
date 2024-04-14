from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        ans = []
        for i in range(len(nums)-1,-1,-1):
            greater_than = sl.bisect_left(nums[i])
            ans.append(greater_than)
            sl.add(nums[i])
        ans.reverse()
        return ans