# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = []
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        while list1.next is not None:
            lst1.append(list1.val)
            list1 = list1.next
        lst1.append(list1.val)
        while list2.next is not None:
            lst1.append(list2.val)
            list2 = list2.next
        lst1.append(list2.val)
        lst1.sort()
        result = ListNode(-101)
        resultHead = result
        
        for i in lst1:
            result.next = ListNode(i)
            result = result.next
        return resultHead.next
            
            
        
                



       