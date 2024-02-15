class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        output = []
        lst = []
        for j in range(len(matrix)):
            for i in matrix:
                lst.append(i[j])
            lst.reverse()
            output.append(lst)
            lst = []
        for i in range(len(matrix)):
            matrix.pop()
        for i in output:
            matrix.append(i)