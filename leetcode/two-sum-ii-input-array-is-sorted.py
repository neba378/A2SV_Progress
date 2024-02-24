class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        i,j = 0,len(nums)-1
        nums.sort()
        while i<j:
            s = nums[i]+nums[j]
            if s == t:
                return [i+1,j+1]
            elif s>t:
                j-=1
            else:
                i+=1
        return []
