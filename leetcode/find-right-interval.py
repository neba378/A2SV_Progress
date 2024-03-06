class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {}
        start = []
        ans = []
        for i in range(len(intervals)):
            dic[intervals[i][0]] = i
            start.append(intervals[i][0])
        start.sort()
        for i in intervals:
            x = bisect_left(start,i[1])
            if x==len(intervals):
                ans.append(-1)
            else:
                ans.append(dic[start[x]])
        return ans
