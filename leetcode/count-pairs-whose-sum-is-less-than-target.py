class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        count = 0
        while i<j:
            if target>nums[i]+nums[j]:
                count+=j-i
                i+=1
            else:
                j-=1
        return count
        