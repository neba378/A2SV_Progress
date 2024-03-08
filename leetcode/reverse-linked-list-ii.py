# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        flag = False
        pre = head
        temp1 = head
        if left == right:
            return head
        for i in range(left-2):
            pre = pre.next
        for i in range(right-2):
            temp1 = temp1.next     
        
        r = temp1.next
        stored = r.next
        if left==1:
            flag = True
            l = pre
            curr = l.next
            l.next = r.next
            temp = l
            n = curr.next
        else:
            l = pre.next
            pre.next = r
            curr = l.next
            l.next = r.next
            r.next = None
            temp = l
            if curr:
                n = curr.next
            else:
                n = None
        while curr and curr!=stored:
            curr.next = temp
            temp = curr
            curr = n
            if curr:
                n = curr.next
        if flag:
            return temp
        return head
