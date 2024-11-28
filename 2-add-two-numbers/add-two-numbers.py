# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # lst1 = []
        # lst2 = []
        # result = ListNode()
        # head = result
        # again = result
        # while l1 is not None:
        #     lst1.append(l1.val)
        #     l1 = l1.next
        # while l2 is not None:
        #     lst2.append(l2.val)
        #     l2 = l2.next
        # lst1.reverse()
        # lst2.reverse()
        # st1 = ""
        # st2 = ""    
        # for i in lst1:
        #     st1 = st1+str(i)
        # for i in lst2:
        #     st2 = st2+str(i)
        # int1 = int(st1)
        # int2 = int(st2)
        # summ = int1 + int2

        # for i in range(len(str(summ))-1, -1,-1):
        #     head.next = ListNode(int(str(summ)[i]))
        #     head = head.next
        # return result.next
        ans = ListNode(0)
        final = ans
        c = 0
        while l1 and l2:
            s = l1.val+l2.val+c
            
            if s>=10:
                v = s-10
                c = 1
                ans.next = ListNode(v)
            else:
                c=0
                ans.next = ListNode(s)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val+c
            
            if s>=10:
                v = s-10
                c = 1
                ans.next = ListNode(v)
            else:
                c=0
                ans.next = ListNode(s)
            ans = ans.next
            l1=l1.next
        while l2:
            s = l2.val+c
            
            if s>=10:
                v = s-10
                c = 1
                ans.next = ListNode(v)
            else:
                c=0
                ans.next = ListNode(s)
            l2 = l2.next
            ans = ans.next
        if c:
            ans.next = ListNode(c)
        return final.next

