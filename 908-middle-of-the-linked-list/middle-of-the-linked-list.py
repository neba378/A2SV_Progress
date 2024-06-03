# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,c = head,0
        while temp:
            temp=temp.next
            c+=1
        ans = head
        for i in range(c//2):
            ans = ans.next
        return ans