class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        res=[]

        def backtrack(i, prev):

            if len(prev) == k:

                res.append(prev.copy())

                return

            for _ in range(i, n+1):

                prev.append(_)

                backtrack(_+1,prev)

                prev.pop()
        backtrack(1,[])
        return res