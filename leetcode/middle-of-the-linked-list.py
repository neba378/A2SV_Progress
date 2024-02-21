# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp is not None:
            l+=1
            temp = temp.next
        for i in range(l//2):
            head = head.next
        return head
        
