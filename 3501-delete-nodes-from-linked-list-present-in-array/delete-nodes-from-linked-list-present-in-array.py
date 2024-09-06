# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        s = set(nums)
        dummy.next = head
        ans = dummy
        while dummy.next:
            if dummy.next.val in s:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return ans.next