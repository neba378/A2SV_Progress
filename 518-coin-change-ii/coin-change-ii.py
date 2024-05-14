class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        lst = [0 for i in range(amount+1)]
        lst[0] = 1
        for c in coins:
            for am in range(1,amount+1):
                if c<=am:
                    lst[am] += lst[am-c]
        return lst[amount]







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

