class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapify(nums)
        self.heap = nums
        self.lst = nlargest(self.k,self.heap)
        heapify(self.lst)

    def add(self, val: int) -> int:
        if len(self.lst)<self.k:
            heappush(self.lst,val)
        elif self.lst[0] < val:
            heapreplace(self.lst,val)
        return self.lst[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)