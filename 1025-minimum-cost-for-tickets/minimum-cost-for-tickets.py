class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = defaultdict(int)
        m = max(days)
        for i in range(len(days)):
            dp[days[i]] = min(dp[days[i]-1]+costs[0],dp[days[i]-7]+costs[1],dp[days[i]-30]+costs[2])
            if i!=len(days)-1:
                for j in range(days[i],days[i+1]):
                    dp[j] = dp[days[i]]
        return dp[m]