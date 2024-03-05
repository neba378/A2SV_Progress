class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        dist = set()
        def rec(arr):
            s = sum(arr)
            if arr and s == target:
                temp = arr[:]
                temp.sort()
                t = tuple(temp)
                if t not in dist:
                    dist.add(t)
                    res.append(arr[:])
            elif s>target:
                return
            for num in candidates:
                arr.append(num)
                rec(arr)
                arr.pop()
        rec([])
        return(res)

