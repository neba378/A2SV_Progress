# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def rec(node, count, left):
            nonlocal ans
            if not node:
                return
            ans = max(ans,count)
            
            if left:
                rec(node.right,count+1,not left)
                rec(node.left,1,left)
            else:
                rec(node.left,count+1,not left)
                rec(node.right,1,left)
        rec(root,0,True)
        rec(root,0,False)
        return ans