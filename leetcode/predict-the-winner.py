class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def current_max(nums,start,end):
            if start == end:
                return nums[start]
            chooseFirst = nums[start] - current_max(nums,start+1,end)
            chooseLast = nums[end] - current_max(nums,start,end-1)
            return max(chooseFirst,chooseLast)
        return current_max(nums,0,len(nums)-1)>=0