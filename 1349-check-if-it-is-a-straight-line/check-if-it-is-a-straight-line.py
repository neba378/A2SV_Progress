class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        c.sort()
        d1,d2 = c[1][0]-c[0][0], c[1][1]-c[0][1]
        for i in range(1,len(c)-1):
            a,b = c[i+1][0]-c[i][0], c[i+1][1]-c[i][1]
            if (b == 0 and d2!=0) or (b != 0 and d2==0):
                return False
            if b == 0 and d2 == 0:
                continue 
            if a/b!=d1/d2:
                return False
        return True
