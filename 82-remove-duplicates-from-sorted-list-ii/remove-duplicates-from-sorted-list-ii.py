# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        st = ListNode(-101)
        st.next = head
        p = head.next
        temp = head
        lst = []
        while p:
            if temp.val == p.val:
                while p and temp.val == p.val:
                    p = p.next
                if not p and temp.next!=None:
                    break
                temp.next = p
                if p:
                    temp = p
                    p = p.next
                if p == None:
                    lst.append(temp)
                
            else:
                lst.append(temp)
                temp = temp.next
                p = p.next
                if not p:
                    lst.append(temp)
        if lst:
            h = lst[0]
            F = False
            for i in range(len(lst)-1):
                F = True
                lst[i].next = lst[i+1]
                lst[i+1].next = None
            if not F:
                h.next = None
        else:
            return None
        return h
