class MinStack:

    def __init__(self):
        self.ma = []
        self.topi = -1
        

    def push(self, val: int) -> None:
        self.ma.append(val)
        self.topi+=1
        

    def pop(self) -> None:
        self.topi-=1
        self.ma.pop()
    def top(self) -> int:
        return self.ma[-1]

    def getMin(self) -> int:
        return min(self.ma)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()