class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        lst = [[k,v] for k,v in counter.items()]
        lst.sort(key=lambda x: -x[1])
        return [lst[i][0] for i in range(k)]