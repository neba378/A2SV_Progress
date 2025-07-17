class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img),len(img[0])
        DIR = [(-1, -1),(-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
        ans = [[0 for i in range(col)] for j in range(row)]
        def inBound(i,j):
            return 0<=i<row and 0<=j<col
        for r in range(row):
            for c in range(col):
                s = img[r][c]
                count = 1
                for dx, dy in DIR:
                    if inBound(r+dx,c+dy):
                        s+=img[r+dx][c+dy]
                        count+=1
                # print(s,count)
                ans[r][c] = (s//count)
        return ans
                
                