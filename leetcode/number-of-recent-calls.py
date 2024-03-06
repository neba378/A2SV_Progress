class RecentCounter:

    def __init__(self):
        self.que = deque()

    def ping(self, t: int) -> int:
        if self.que:
            while self.que and t-3000>self.que[0]:
                self.que.popleft()
            while self.que and t<self.que[-1]:
                self.que.pop()
            self.que.appendleft(t-3000)
            self.que.append(t)
        else:
            self.que.append(t-3000)
            self.que.append(t)
        return len(self.que)-1
        




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)