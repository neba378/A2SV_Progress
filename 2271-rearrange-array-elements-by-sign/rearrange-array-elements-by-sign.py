class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i,j = 0,0
        ans = [0]*len(nums)
        c = 0
        while i<len(nums):
            if nums[i]>0:
                ans[2*c] = nums[i]
                c+=1
            i+=1
        c= 0
        while j<len(nums):
            if nums[j]<0:
                ans[2*c+1] = nums[j]
                c+=1
            j+=1
        return ans


