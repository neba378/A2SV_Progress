class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        s = nums
        def rec(s,curr):
            if len(s) > 0:
                if curr[:] not in res:
                    res.append(curr[:])
            if len(s) == 0:
                if curr[:] not in res:
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