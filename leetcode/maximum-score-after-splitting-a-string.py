class Solution:
    def maxScore(self, s: str) -> int:
        countOne = [0]
        countZero = [0]
        for i in s:
            if i == "0":
                countZero.append(countZero[-1]+1)
            else:
                countZero.append(countZero[-1])
        for j in range(len(s)-1,-1,-1):
            if s[j] == "1":
                countOne.append(countOne[-1]+1)
            else:
                countOne.append(countOne[-1])
        countOne.reverse()
        print(countOne,countZero)
        maxi = 0
        for i in range(len(countOne)):
            if i!=0 and i!=len(countOne)-1:
                maxi = max(maxi,countOne[i]+countZero[i])
        return maxi
        