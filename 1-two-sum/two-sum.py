class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        dic = defaultdict(list)
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return dic[target-nums[i]][0],i
            dic[nums[i]].append(i)
        return [-1,-1]
