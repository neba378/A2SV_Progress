"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        l = [[root]]
        while queue:
            lst = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    lst.append(node.left)
                if node.right:
                    queue.append(node.right)
                    lst.append(node.right)
            l.append(lst)
        for lst in l:
            for i in range(len(lst)):
                if i != len(lst)-1:
                    lst[i].next = lst[i+1]
        return root

        return 

