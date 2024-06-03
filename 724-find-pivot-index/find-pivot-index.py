class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans = -1
        pre = [0]
        post = [0]
        for i in range(len(nums)):
            pre.append(pre[-1]+nums[i])
        for i in range(len(nums)-1,-1,-1):
            post.append(post[-1]+nums[i])
        post.reverse()
        post.pop()
        pre = pre[1:]
        for i in range(len(nums)):
            if pre[i] == post[i]:
                return i
        return ans

