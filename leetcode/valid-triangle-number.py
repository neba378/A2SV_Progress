class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        c = 0
        if len(nums)<3:
            return 0
        for i in range(2,len(nums)):
            l,r = 0, i-1
            while(l<r):
                two = nums[l]+nums[r]
                if two>nums[i]:
                    c+=(r-l)
                    r-=1
                else:
                    l+=1
        return c