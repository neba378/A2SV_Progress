# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_node = ListNode(0)
        new_node.next = head
        c = 0
        if head.next == None:
            return None
        while(new_node.next is not None):
            new_node = new_node.next
            c+=1
        new_node = ListNode(0)
        new_node.next = head
        if c == n:
            head = head.next
            return head
        for i in range(c-n):
            new_node = new_node.next
        new_node.next = new_node.next.next
        return head
        
        