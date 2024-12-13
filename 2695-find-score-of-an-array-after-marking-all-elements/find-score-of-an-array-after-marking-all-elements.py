class Solution:
    def findScore(self, nums: List[int]) -> int:
        dic = {i:nums[i] for i in range(len(nums))}
        heap = [(nums[i],i) for i in range(len(nums))]
        heapify(heap)
        ans = 0
        while heap:
            num = heappop(heap)
            if num[1] in dic:
                ans+= num[0]
                del dic[num[1]]
                if num[1]+1 in dic:
                    del dic[num[1]+1]
                if num[1]-1 in dic:
                    del dic[num[1]-1]
                
        return ans