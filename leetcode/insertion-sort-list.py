# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        temp = head
        res = head
        while head:
            lst.append(head.val)
            head = head.next
        lst.sort()
        i = 0
        while temp:
            temp.val = lst[i]
            i+=1
            temp = temp.next
        return res