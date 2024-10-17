class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = [_ for _ in str(num)]
        maxi = 0
        idx = -1
        for i in range(1,len(numStr)):
            if int(numStr[i])>int(numStr[i-1]) or maxi == int(numStr[i]):
                if maxi<=int(numStr[i]):
                    maxi = int(numStr[i])
                    idx = i
        if idx == -1:
            return num
        for i in range(len(numStr)):
            if maxi>int(numStr[i]):
                numStr[idx], numStr[i] = numStr[i], numStr[idx]
                return int("".join(numStr))
        return num
