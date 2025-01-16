class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2 = len(nums1),len(nums2)
        dic = defaultdict(int)
        for num in nums1:
            dic[num]+=l2
        for num in nums2:
            dic[num]+=l1
        x = 0
        for num in dic:
            if dic[num]%2:
                x^=num
        return x
        