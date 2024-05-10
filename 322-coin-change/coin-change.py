class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        lst = [float("inf") for i in range(amount+1)]
        lst[0] = 0

        for am in range(amount+1):
            for c in coins:
                if c<=am:
                    lst[am] = min(lst[am],lst[am-c]+1)
        if lst[amount] == float("inf"):
            return -1
        return lst[amount]
