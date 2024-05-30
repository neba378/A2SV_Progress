class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k
        nums.sort(reverse=True)
        n = len(nums)
        bucket = [0] * k
        def bt(idx):
            if idx == n:
                return True
            for i in range(k):
                if bucket[i] + nums[idx] <= target:
                    bucket[i] += nums[idx]
                    if bt(idx + 1):
                        return True
                    bucket[i] -= nums[idx]
                    if bucket[i] == 0:
                        break
            return False
        return bt(0)