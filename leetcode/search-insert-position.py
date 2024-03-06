class Solution:
    def searchInsert(self, l: List[int], target: int) -> int:
        return bisect_left(l,target)