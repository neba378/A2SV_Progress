# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        my_k = 1
        val = -1
        def inOrder(root,k):
            nonlocal my_k
            nonlocal val
            if not root:
                return None
            inOrder(root.left,k)
            
            if k == my_k:
                val = root.val
            my_k+=1
            inOrder(root.right,k)
        inOrder(root,k)
        return val
            