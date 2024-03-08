# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA = headA
        nodeB = headB
        visited = set()
        while nodeA:
            visited.add(nodeA)
            nodeA = nodeA.next
        while nodeB:
            if nodeB in visited:
                return nodeB
            nodeB = nodeB.next
        
