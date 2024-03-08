class Solution:
    def predictPartyVictory(self, s: str) -> str:
        R = deque()
        D = deque()
        for i in range(len(s)):
            if s[i] == "R":
                R.append(i)
            else:
                D.append(i)
        i = 0
        while D and R:
            r = R.popleft()
            d = D.popleft()
            if r<d:
                R.append(r+len(s))
            else:
                D.append(d+len(s))
        print(D,R)
        if len(R)>len(D):
            return "Radiant"
        return "Dire"
            


        
        