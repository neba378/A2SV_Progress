class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        memo = {}
        def topDown(ind1,mask):
            if (ind1,mask) not in memo:
                if ind1 == n:
                    return 0
                mini = float("inf")
                for i in range(n):
                    if mask & (1<<i) == 0:
                        mini = min(mini,(nums1[ind1]^nums2[i])+topDown(ind1+1,mask|(1<<i)))
                memo[(ind1,mask)] = mini
            return memo[(ind1,mask)]
        return topDown(0,0)

            


