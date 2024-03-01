# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        s = set()
        while slow:
            s.add(slow)
            slow = slow.next
            if slow and slow in s:
                return slow
        return None