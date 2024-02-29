# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        elif not q or not p:
            return False
        if q.val != p.val:
            return False
        a = self.isSameTree(p.left,q.left)
        b = self.isSameTree(p.right,q.right)
        return a and b
        