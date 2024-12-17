class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        lst = [[nums[i],i] for i in range(len(nums))]
        heapify(lst)
        for i in range(k):
            num = heappop(lst)
            heappush(lst,[num[0]*multiplier,num[1]])
        lst.sort(key=lambda x: x[1])
        for i in range(len(lst)):
            lst[i] = lst[i][0]
        return lst