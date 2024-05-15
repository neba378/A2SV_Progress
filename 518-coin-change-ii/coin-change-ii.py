class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(ind,am):
            if am == 0:
                return 1
            if am<0 or ind>=len(coins):
                return 0
            if (ind,am) not in memo:
                memo[(ind,am)] = dp(ind+1,am)+dp(ind,am-coins[ind])
            return memo[(ind,am)]
        return dp(0,amount)







        # lst = []
        # s = set()
        # def bt(am):
        #     nonlocal c
        #     if sum(lst)>am:
        #         return
        #     if sum(lst) == am:
        #         if "".join(lst) not in s:
        #             c+=1
        #             s.add("".join(lst))
        #         return
            
        #     for i in range(len(coins)):
        #         lst.append(coins[i])
        #         bt(am)
        #         lst.pop()
        # c = 0
        # bt(amount)
        # print(c,lst)
        # return 4

