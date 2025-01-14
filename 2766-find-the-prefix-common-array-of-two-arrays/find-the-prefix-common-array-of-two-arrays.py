class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        aSet = set()
        count = 0
        bSet = set()
        for i in range(len(A)):
            aSet.add(A[i])
            bSet.add(B[i])
            if A[i] == B[i]:
                count+=1
            elif A[i] in bSet and B[i] in aSet:
                count+=2
            elif A[i] in bSet or B[i] in aSet:
                count+=1
            C.append(count)
        return C
    
