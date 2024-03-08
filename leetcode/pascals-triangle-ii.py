class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1,1]
        for j in range(rowIndex-1):
            lst = [1]
            for i in range(1,len(row)):
                lst.append(row[i]+row[i-1])
            lst.append(1)
            row = lst
        return row
        