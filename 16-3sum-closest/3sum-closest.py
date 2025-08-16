class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        val = 0
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1 
            while(l<r):
                sumy = nums[i]+nums[l]+nums[r]
                # print(nums[i],nums[l],nums[r])
                if abs(sumy-target) < ans:
                    val = sumy
                ans = min(ans,abs(sumy-target))
                # print(ans,sumy)
                if sumy == target:
                    return sumy
                elif sumy > target:
                    r-=1
                else:
                    l+=1
        return val
                

        