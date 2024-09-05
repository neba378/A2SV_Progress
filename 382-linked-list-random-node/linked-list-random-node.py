# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        temp = self.head
        n=0
        while temp:
            n+=1
            temp = temp.next
        rand = random.randint(1,n)
        temp = self.head
        for i in range(rand-1):
            temp = temp.next
        return temp.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()