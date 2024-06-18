# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        temp = l1
        while temp:
            num1+=str(temp.val)
            temp = temp.next
        
        temp = l2
        while temp:
            num2+=str(temp.val)
            temp = temp.next
       
        ans = str(int(num1)+int(num2))
        answer = ListNode(int(ans[0]))
        temp = answer
        for i in range(1,len(ans)):
            temp.next = ListNode(int(ans[i]))
            temp = temp.next
        return answer