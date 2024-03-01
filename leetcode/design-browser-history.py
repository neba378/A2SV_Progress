class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None    

class BrowserHistory:


    def __init__(self, homepage: str):
        self.head = Node(homepage)
        print("in init",self.head.data)
    def visit(self, url: str) -> None:
        new = Node(url)
        self.head.next = new
        new.prev = self.head
        self.head = new
    def back(self, steps: int) -> str:
        while self.head and self.head.prev and steps>0:
            self.head = self.head.prev
            steps-=1
        return self.head.data



    def forward(self, steps: int) -> str:
        while self.head and self.head.next and steps>0:
            steps-=1
            self.head = self.head.next
        return self.head.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)