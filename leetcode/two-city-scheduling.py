class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:abs(x[1]-x[0]), reverse=True)
        a,b = 0,0
        tot = 0
        half = len(costs)//2
        for i,j in costs:
            if i<=j:
                if a<half:
                    a+=1
                    tot+=i
                else:
                    tot+=j
                    b+=1
            else:
                if b<half:
                    b+=1
                    tot+=j
                else:
                    tot+=i
                    a+=1
                    
        return tot
                
                



