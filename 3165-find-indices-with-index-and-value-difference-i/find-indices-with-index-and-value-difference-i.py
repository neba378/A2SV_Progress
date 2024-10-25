class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        i,j = 0,indexDifference
        while i<len(nums):
            if j<len(nums) and abs(nums[i]-nums[j])>=valueDifference:
                return [i,j]
            else:
                if j<len(nums)-1:
                    j+=1
                else:
                    i+=1
                    j = i+indexDifference
        return [-1,-1]

