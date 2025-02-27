class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        def xOr(nums):
            ans = 0
            for num in nums:
                ans^=num
            return ans
        n1,n2 = len(nums1),len(nums2)
        if n1%2 == 0 and n2%2 == 0:
            return 0
        if n1%2 == 0 and n2%2 != 0:
            return xOr(nums1)
        if n1%2 != 0 and n2%2 == 0:
            return xOr(nums2)
        return xOr(nums1+nums2)
        

