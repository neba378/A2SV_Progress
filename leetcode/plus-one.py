class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strDigit = ""
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            for i in digits:
                strDigit+=str(i)
            intDigit = int(strDigit)+1
            strDigit = str(intDigit)
            lst = [int(x) for x in strDigit]
            return (lst)