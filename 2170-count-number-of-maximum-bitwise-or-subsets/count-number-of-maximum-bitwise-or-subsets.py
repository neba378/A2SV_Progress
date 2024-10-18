class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        def findSubset(nums,lst,ind):
            res.append(lst[:])
            for i in range(ind,len(nums)):
                lst.append(nums[i])
                findSubset(nums,lst,i+1)
                lst.pop()
            return res
        findSubset(nums,[],0)
        dic = defaultdict(int)
        for lst in res:
            if lst:
                ans = 0
                for num in lst:
                    ans|=num
                dic[ans]+=1
        return dic[max(dic)]
