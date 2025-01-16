class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2 = len(nums1),len(nums2)
        x = 0
        if l2%2:
            for num in nums1:
                x^=num
        if l1%2:
            for num in nums2:
                x^=num
        return x
        