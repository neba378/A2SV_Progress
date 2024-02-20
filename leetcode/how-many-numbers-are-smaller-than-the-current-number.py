class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = [0]
        temp = nums[:]
        nums.sort()
        dic = defaultdict(int)
        dic[nums[0]] = 0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dic[nums[i]] = i
        print(dic)
        for i in range(len(temp)):
            temp[i] = dic[temp[i]]
        return temp