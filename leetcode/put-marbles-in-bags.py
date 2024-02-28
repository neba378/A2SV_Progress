class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        lst = []
        for i in range(1,len(weights)):
            lst.append(weights[i]+weights[i-1])
        lst.sort()
        mini = 0
        maxi = 0
        mini = sum(lst[:k-1])
        if k!=1:
            maxi = sum(lst[-k+1:])
       
        return maxi-mini