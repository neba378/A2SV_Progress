class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = 0
        count = 0
        cz = 0
        for j in range(len(answerKey)):
            if answerKey[j] == 'F':
                cz+=1
            while cz>k:
                if answerKey[i] == 'F':
                    cz-=1
                i+=1          
            count = max(count,j-i+1)
        i = 0
        countT = 0
        ct = 0
        for j in range(len(answerKey)):
            if answerKey[j] == 'T':
                ct+=1
            while ct>k:
                if answerKey[i] == 'T':
                    ct-=1
                i+=1          
            countT = max(countT,j-i+1)

        return max(count,countT)
