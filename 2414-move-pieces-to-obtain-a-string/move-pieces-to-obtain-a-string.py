class Solution:
    def canChange(self, start: str, target: str) -> bool:
        q1 = []
        q2 = []

        for i in range(len(start)):
            if start[i]!="_":
                q1.append((start[i],i))
            if target[i]!="_":
                q2.append((target[i],i))
        if len(q1)!=len(q2):
            return False
        while len(q1)>0:
            q1v, ind1 = q1.pop(0)
            q2v, ind2 = q2.pop(0)

            if q1v!=q2v or (q1v == "L" and ind1<ind2 ) or (q1v == "R" and ind1>ind2):
                return False
        return True
