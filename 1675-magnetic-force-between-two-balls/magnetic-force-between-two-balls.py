class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        def place(val):
            count = 1  
            last_position = pos[0]
            
            for i in range(1, len(pos)):
                if pos[i] - last_position >= val:
                    count += 1
                    last_position = pos[i]  
                if count == m:
                    return True
            return False

        diff = []
        pos.sort()
        for i in range(1,len(pos)):
            diff.append(pos[i]-pos[i-1])
        left = min(diff)
        right = pos[-1]-pos[0]
        while left<=right:
            mid = (right+left)//2
            if place(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans
