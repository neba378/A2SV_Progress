class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        '''
        Brute force
        '''
        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     for j in range(i,n):
        #         if nums[j]>=nums[i]:
        #             ans = max(ans,j-i)
        # return ans
        n = len(nums)
        ans = 0
        Mstack = [nums[-1]]
        for i in range(n-2,-1,-1):
            Mstack.append(max(Mstack[-1],nums[i]))
        Mstack.reverse()
        l,r = 0,0
        while l<n and r<n:
            if Mstack[r]>=nums[l]:
                ans = max(ans,r-l)
                r+=1
            else:
                l+=1
        return ans
        
