# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b == 0:
                return a
            else:
                return gcd(b,a%b)
        t = head
        while t.next:
            temp = t.next
            value = ListNode(gcd(t.val,t.next.val))
            t.next = value
            value.next = temp
            t = t.next.next
        return head


