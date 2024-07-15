# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = [[root.val]]
        while queue:
            lst = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    lst.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    lst.append(node.right.val)
            ans.append(lst)
        return ans[-2][0]