from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        alwaysSortingList = SortedList()
        count = 0
        for i in range(len(nums1)):
            bigger_than = alwaysSortingList.bisect_right(nums1[i]-nums2[i]+diff)
            count+=bigger_than
            alwaysSortingList.add(nums1[i]-nums2[i])
        return count