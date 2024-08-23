# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, dist: int) -> int:
        self.ans = 0
        def rec(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [1]
            left = rec(root.left)
            right = rec(root.right)

            for l in left:
                for r in right:
                    if l+r<=dist:
                        self.ans+=1
            return [i+1 for i in left+right]
        rec(root)
        return self.ans