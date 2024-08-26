"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        lst = []
        def rec(node):
            if not node.children:
                return
            for i in node.children:
                rec(i)
                lst.append(i.val)
        if not root:
            return None
        rec(root)
        lst.append(root.val)
        return lst
