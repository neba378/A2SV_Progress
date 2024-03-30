class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 1
        j = 0
        ans = []
        l = len(nums)
        nums = list(set(nums))
        nums.sort()
        while i<=l:
            if j<len(nums) and nums[j] != i:
                ans.append(i)
                j-=1
            elif j>=len(nums):
                ans.append(i)
                j-=1
            i+=1
            j+=1
        
        return ans
            
                