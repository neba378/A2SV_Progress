class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        d = 0 #it was facing north first
        ans = 0
        x,y = 0,0
        Set = set(tuple(i) for i in obstacles)
        
            
        for i in commands:
            if i == -1:
                d = (d+1)%4
            elif i == -2:
                d = (d-1)%4
            else:
                dx,dy = DIR[d]
                for _ in range(i):
                    if (x+dx,y+dy) not in Set:
                        x+=dx
                        y+=dy
                    else:
                        break
                ans = max(ans,x**2+y**2)
        return ans
                    
                    


