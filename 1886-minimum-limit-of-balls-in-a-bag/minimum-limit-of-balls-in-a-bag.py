class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)
        while left<right:
            op = 0
            mid = (left+right)//2
            for num in nums:
                op+=math.ceil(num/mid)-1
            if op>maxOperations:
                left = mid+1
            else:
                right = mid
        return left
                    
                
