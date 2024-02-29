# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def cla(root,p,q):
            count = 100000
            if not root:
                return None
            if root.val == p.val:
                count = min(count,root.val)
                print(count)
                return TreeNode(count)
            elif root.val>p.val and root.val>q.val:
                count = min(count,root.val)
                return cla(root.left,p,q)
            elif root.val<p.val and root.val<q.val:
                count = min(count,root.val)
                return cla(root.right,p,q)
            else:
                return TreeNode(min(count,root.val))
        return cla(root,p,q)
