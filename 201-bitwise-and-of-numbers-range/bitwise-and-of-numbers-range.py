class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bigBin = bin(right)[2:]
        smallBin = bin(left)[2:]
        smallBin = "0"*(len(bigBin)-len(smallBin))+smallBin
        l = len(bigBin)
        f = False
        for i in range(l):
            if bigBin[i] == "1" and smallBin[i] == "0":
                f = True
                break
        if not f:
            return(int(bigBin,2))
        bigBin = bigBin[:i]+"0"*(l-i)
        smallBin = smallBin[:i]+"0"*(l-i)
        anded = int(bigBin,2) & int(smallBin,2)
        return anded
