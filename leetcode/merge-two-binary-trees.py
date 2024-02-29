# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1,root2):
            if not root1 and not root2:
                return None
            elif not root1 and root2:
                return root2
            elif not root2 and root1:
                return root1
            else:
                res = TreeNode(root2.val+root1.val)
                res.left = merge(root1.left, root2.left)
                res.right = merge(root1.right, root2.right)
            return res
        return merge(root1,root2)
        