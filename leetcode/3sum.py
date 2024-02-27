class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i,j in enumerate(nums):
            if i!=0 and j == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while(l<r):
                s = j+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    ans.append([nums[l],j,nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return ans

        