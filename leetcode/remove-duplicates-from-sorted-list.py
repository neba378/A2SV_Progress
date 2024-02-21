# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head
        
        if not head:
            return head
        temp2 = head.next
        while temp2:
            if temp1.val == temp2.val:
                temp1.next = temp2.next
                temp2 = temp1.next
            else:
                temp1 = temp1.next
                temp2 = temp2.next
        return head