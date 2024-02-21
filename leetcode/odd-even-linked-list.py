# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = ListNode(head.val)
        one  = first
        
        second = ListNode(head.next.val)
        two = second
        temp = head
        while temp:
            first.next = ListNode(temp.val)
            first = first.next
            if temp.next:
                temp = temp.next.next
            else:
                break
        temp = head.next
        while temp:
            second.next = ListNode(temp.val)
            second = second.next
            if temp.next:
                temp = temp.next.next
            else:
                break
        if two.next:
            first.next = two.next
        return one.next
