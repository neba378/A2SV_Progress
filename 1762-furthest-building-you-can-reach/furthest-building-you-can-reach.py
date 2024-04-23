class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladder: int) -> int:
        diff = []
        for i in range(len(heights)-1):
            d = heights[i+1]-heights[i]
            if d<=0:
                continue
            bricks-=d
            heappush(diff,-d)
        
            if bricks<0:
                if ladder == 0:
                    return i
                ladder-=1
                bricks-=heappop(diff)
        return len(heights)-1
                
                
            
        