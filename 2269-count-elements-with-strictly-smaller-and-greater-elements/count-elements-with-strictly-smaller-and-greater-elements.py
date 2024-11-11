class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        while i<len(nums)-1:
            if nums[i] != nums[i+1]:
                break
            i+=1
        while j>0:
            if nums[j] != nums[j-1]:
                break
            j-=1
        return j-i-1 if j-i-1>0 else 0