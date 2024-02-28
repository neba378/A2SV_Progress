class Solution:
    def trap(self, height: List[int]) -> int:
        i,sum = 0,0
        j = len(height)-1
        last = len(height)
        totSum = 0
        left_max = 0
        right_max = 0
        while i<j:
            if height[i]<height[j]:
                if left_max<height[i]:
                    left_max = height[i]
                else:
                    totSum+= left_max-height[i]
                i+=1
            else:
                if right_max<height[j]:
                    right_max = height[j]
                else:
                    totSum+=(right_max-height[j])
                j-=1
        return totSum