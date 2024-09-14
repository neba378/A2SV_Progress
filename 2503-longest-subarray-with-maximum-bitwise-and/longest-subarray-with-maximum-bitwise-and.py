class Solution(object):
    def longestSubarray(self, nums):
        max_consecutive_count = 0
        current_count = 0
        
        largest_element = max(nums)
        
        for num in nums:
            if num == largest_element:
                current_count += 1
            else:
                current_count = 0
            
            max_consecutive_count = max(max_consecutive_count, current_count)
        
        return max_consecutive_count