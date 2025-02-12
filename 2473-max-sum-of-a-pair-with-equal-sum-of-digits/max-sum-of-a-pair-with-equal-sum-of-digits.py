class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        ans = -1
        for num in nums:
            dic[sum(int(_) for _ in str(num))].append(num)
        for k in dic:
            if len(dic[k])>1:
                dic[k].sort()
                ans = max(ans,dic[k][-1]+dic[k][-2])
        return ans
