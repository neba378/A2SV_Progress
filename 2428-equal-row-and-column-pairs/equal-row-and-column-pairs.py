class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def mult(a,b):
            return a*b
        sRow = defaultdict(int)
        sCol = defaultdict(int)
        for i in range(len(grid)):
            sRow[tuple(grid[i])]+=1
        for i in range(len(grid)):
            lst = []
            for j in range(len(grid[0])):
                lst.append(grid[j][i])
            sCol[tuple(lst)]+=1
        ans = 0

        for i in sRow:
            if i in sCol:
                ans+=mult(sRow[i],sCol[i])
        return ans