class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        lst = []
        output = []
        for j in range(len(matrix[0])):
            for i in matrix:
                lst.append(i[j])
            output.append(lst)
            lst = []
        return output