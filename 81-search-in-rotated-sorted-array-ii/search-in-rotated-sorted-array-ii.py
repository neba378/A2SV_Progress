class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i,j = 0,len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid] == target:
                return True
            
            if nums[mid]==nums[i]:
                i+=1
                continue
            if nums[i]<=nums[mid]:
                if nums[i]<= target <=nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            else:
                if nums[mid]<=target<=nums[j]:
                    i = mid+1
                else:
                    j = mid-1
        return False

