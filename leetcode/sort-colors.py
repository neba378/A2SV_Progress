class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        i = 0
        for k in range(3):
            for j in range(counter[k]):
                    nums[i] = k
                    i+=1
        


