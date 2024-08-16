class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort()
        maxi = max(c[-1] for c in arrays[1:])
        return max(abs(maxi-arrays[0][0]),abs(arrays[0][-1]-arrays[1][0]))