class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for i in nums2:
            while stack and stack[-1]<i:
                dic[stack.pop()] = i
            else:
                stack.append(i)
        for i in stack:
            dic[i] = -1
        ans = []
        for i in nums1:
            ans.append(dic[i])
        return ans