class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = set(nums)
        def rec(s,curr):
            if len(s) > 0:
                res.append(curr[:])
            if len(s) == 0:
                res.append(curr[:])
                return
            new_num = s.copy()
            for num in s:
                new_num.remove(num)
                curr.append(num)
                rec(new_num,curr)
                curr.remove(num)
        rec(s,[])
        return  res


    
