class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = [0]+ list(accumulate(nums))
        hash = {}
        count = 0
        sum = 0
        # for i in range(len(preSum)):
        #     for j in range(i):
        #         if preSum[i]-preSum[j] == k:
        #             count+=1
        # return count
        for i in range(len(nums)):
            sum+=nums[i]
            if sum == k:
                count += 1
            if sum-k in hash:
                count += hash[sum-k]
            if sum not in hash:
                hash[sum] = 1
            else:
                hash[sum]+=1
        return count
        
