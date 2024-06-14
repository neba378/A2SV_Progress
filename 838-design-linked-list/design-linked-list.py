class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None  

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        lst = []
        while temp:
            lst.append(temp.data)
            temp = temp.next

        if index>=len(lst):
            return -1
        print(lst)
        return lst[index]

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        if not self.head:
            self.head = temp
            return
        temp.next = self.head
        self.head = temp
        print("from the add at head:",self.head)


    def addAtTail(self, val: int) -> None:
        temp1 = self.head
        temp = Node(val)
        if not self.head:
            self.head = temp
            return
        while temp1.next:
            temp1 = temp1.next
        temp1.next = temp
        print("from the add at tail:",self.head)
    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        temp1 = Node(val)
        i = 1
        if index == 0:
            self.addAtHead(val)
            return
        while temp:
            if i!=index:
                temp = temp.next
                i+=1
            else:
                break
        
        if not temp and i<=index:
            return 
        if temp.next == None:
            temp.next = temp1
        else:
            temp1.next = temp.next
            temp.next = temp1
        print("from the add at index:",self.head)
    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        i = 1
        if index == 0:
            self.head = self.head.next
            return
        while temp:
            if i!=index:
                temp = temp.next
                i+=1
            else:
                break

        if not temp: 
            return 
            
        if temp and temp.next == None:
            temp = None
        else:
            temp.next = temp.next.next

        print("from the delete at index:",self.head)
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)