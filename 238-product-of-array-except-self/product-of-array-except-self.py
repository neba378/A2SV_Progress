class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        for i in range(len(nums)-1):
            if i == 0:
                pre.append(nums[i])
                continue
            pre.append(pre[-1]*nums[i])    
        for i in range(len(nums)-1,0,-1):
            if i == len(nums)-1:
                post.append(nums[i])
                continue
            post.append(post[-1]*nums[i]) 
        post.reverse()
        
        ans = [0]*len(nums)
        print(pre,post)
        for i in range(len(nums)):
            ans[i] = pre[i]*post[i]
        return ans            

        