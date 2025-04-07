class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans = meetings[0][0]-1
        maxi = 0
        if len(meetings) == 1:
            return ans + days-meetings[0][1]
        for i in range(len(meetings)-1):
            maxi = max(meetings[i][1],maxi)
            if maxi< meetings[i+1][0]:
                ans+=meetings[i+1][0]-1 - maxi
            else:
                continue
        maxi = max(meetings[i+1][1],maxi)
        return ans + days-maxi
