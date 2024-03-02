class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = 10**5+1
        i = 0
        s = 0
        for j in range(len(nums)):
            s+= nums[j]
            if s >= target:
                length = min(length,j-i+1)
            while i<j and s>=target:             
                s-=nums[i]
                i+=1
                if s>=target:
                    length = min(length,j-i+1)
        if length == 10**5+1:
            return 0
        return length