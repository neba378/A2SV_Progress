class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        l = len(rolls)+n
        s = sum(rolls)
        x = l*mean-s
        if x>n*6 or x<(n):
            return []
        else:
            quo = x//n
            final = quo*n
            less = x-final
            if less == 0:
                return [quo]*n
            else:
                lst = [quo]*(n-1)
                if less+quo>6:
                    print("eyes")
                    for i in range(less+quo-6):
                        lst[i]+=1
                    return lst + [6]

                return lst + [less+quo] 
        return []