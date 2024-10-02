class Solution:
    def arrayRankTransform(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        temp = nums.copy()
        temp.sort()
        dic = {}
        r = 1
        dic[temp[0]] = 1
        for i in range(1,len(nums)):
            if temp[i] != temp[i-1]:
                r+=1
            dic[temp[i]] = r
        return [dic[i] for i in nums]


        