class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans = []
        i = 0

        for j in range(1, len(intervals)):
            if intervals[j][0] > intervals[i][1]:
                ans.append([intervals[i][0], intervals[i][1]])
                i = j  
            else:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])

        ans.append([intervals[i][0], intervals[i][1]])
        return ans
