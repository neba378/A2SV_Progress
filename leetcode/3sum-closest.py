class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mini = float('inf')
        val = 3000
        for i,j in enumerate(nums):
            if i!=0 and j == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while(l<r):
                s = j+nums[l]+nums[r]
                if abs(target-s)<mini:
                    val = s
                mini = min(mini,abs(target-s))
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    l+=1
                    return target
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return val