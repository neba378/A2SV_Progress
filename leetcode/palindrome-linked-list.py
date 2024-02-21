# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while(head is not None):
            lst.append(head.val)
            head = head.next
        start = 0
        end = len(lst)-1
        while(start<=end):
            if lst[start]!=lst[end]:
                return False
            else:
                start+=1
                end-=1
        return True