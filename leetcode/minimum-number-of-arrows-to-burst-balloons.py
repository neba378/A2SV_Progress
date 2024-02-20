class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # start = [points[0]]
        # for i,j in points:
        #     if i<=start[-1][1] and i>=start[-1][0]:
        #         continue
        #     elif j<=start[-1][1] and j>=start[-1][0]:
        #         continue
        #     else:
        #         start.append([i,j])
        #     if i<start[-1][0]:
        #         start[-1][0]=i
        #     if j>start[-1][1]:
        #         start[-1][1]=j
        
        # return len(start)
        points.sort(key=lambda x:x[1])
        end = points[0][1]
        count = 1
        for i,j in points:
            if i>end:
                end = j
                count+=1
        return count
