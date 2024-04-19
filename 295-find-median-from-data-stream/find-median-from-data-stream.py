from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.arr = SortedList()
        self.isEven = True


    def addNum(self, num: int) -> None:
        self.arr.add(num)
        self.isEven = not self.isEven

    def findMedian(self) -> float:
        if self.isEven:
            mid = len(self.arr)//2
            return (self.arr[mid]+self.arr[mid-1])/2
        else:
            mid = len(self.arr)//2
            return self.arr[mid]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()