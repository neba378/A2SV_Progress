class MyStack:

    def __init__(self):
        self.arr = [0]*101
        self.pointer = -1

    def push(self, x: int) -> None:
        self.pointer+=1
        self.arr[self.pointer]=x
        

    def pop(self) -> int:
        self.pointer-=1
        
        return self.arr[self.pointer+1]
        
        

    def top(self) -> int:
        
        return self.arr[self.pointer]

    def empty(self) -> bool:
        return self.pointer == -1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()