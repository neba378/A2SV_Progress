# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
       
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.diff = 0
        def checker(node, maxi, mini):
            if not node:
                self.diff = max(self.diff, maxi - mini)
                return
            checker(node.left, max(maxi, node.val), min(mini, node.val))
            checker(node.right, max(maxi, node.val), min(mini, node.val))
        checker(root,-1,100001)
        return self.diff

