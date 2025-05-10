class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def check(n1,n2):
            if sum(n2)<sum(n1):
                return True
            return False
        rep1 = []
        rep2 = []
        for i in range(len(nums1)):
            if nums1[i] == 0:
                rep1.append(1)
            else:
                rep1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] == 0:
                rep2.append(1)
            else:
                rep2.append(nums2[i])
        if 0 not in nums1 and check(rep2,nums1):
            return -1
        if 0 not in nums2 and check(rep1,nums2):
            return -1
        return max(sum(rep1),sum(rep2))