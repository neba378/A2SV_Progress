# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        lst = []
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l+=1
        temp = head
        temp2 = temp
        third = temp
        if l<=k:
            while temp:
                temp2 = temp2.next
                temp.next = None
                lst.append(temp)
                temp = temp2
                k-=1
            while k>0:
                lst.append(None)
                k-=1    
        else:
            q = l//k
            r = l%k
            for i in range(k):
                if r>0:
                    for i in range(q):
                        temp = temp.next
                    r-=1
                    temp2 = temp.next
                    temp.next = None
                    lst.append(third)
                    third = temp2
                    temp = temp2
                else:
                    for i in range(q-1):
                        temp = temp.next
                    temp2 = temp.next
                    temp.next = None
                    lst.append(third)
                    third = temp2
                    temp = temp2

        return lst