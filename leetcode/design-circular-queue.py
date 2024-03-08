class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1]*k
        self.front = -1
        self.rear = -1


    def enQueue(self, value: int) -> bool:
        if self.front == -1:
            self.front+=1
        if -1 in self.queue:
            if self.rear==len(self.queue)-1:
                self.rear = (self.rear+1)%len(self.queue)
            else:
                self.rear+=1
            self.queue[self.rear] = value
            print(self.queue)
            return True
        return False

    def deQueue(self) -> bool:
        
        if self.queue[self.front] == -1:
            return False
        self.queue[self.front] = -1
        if self.front==len(self.queue)-1:
                self.front = (self.front+1)%len(self.queue)
        else:
            self.front+=1
        return True

    def Front(self) -> int:
        return self.queue[self.front]

    def Rear(self) -> int:
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1 or self.queue[self.front] == -1

    def isFull(self) -> bool:
        return self.queue[self.front]!=-1 and (self.rear+1)%len(self.queue)==self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()