class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dist = len(set(nums))
        c = 0
        ind = 0
        counter = Counter()
        for i in nums:
            counter[i]+=1
            while(len(counter) == dist):
                counter[nums[ind]]-=1
                if counter[nums[ind]] == 0:
                    del counter[nums[ind]]
                ind+=1
            c+=ind
        return c