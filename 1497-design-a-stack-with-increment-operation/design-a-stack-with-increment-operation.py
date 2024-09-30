class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [-1]*maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top+1<len(self.stack):
            self.stack[self.top+1] = x
            self.top+=1

    def pop(self) -> int:
        if self.top != -1:
            self.top-=1
            return self.stack[self.top+1]
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.top+1>=k:
            for i in range(k):
                self.stack[i]+=val
        else:
            if self.top>-1:
                for i in range(self.top+1):
                    self.stack[i]+=val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)