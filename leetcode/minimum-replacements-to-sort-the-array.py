class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)-2, -1,-1):
            if nums[i]<nums[i+1]:
                continue
            num_of_elem = ceil(nums[i]/nums[i+1])
            answer+=num_of_elem-1
            nums[i]//=num_of_elem
        return answer