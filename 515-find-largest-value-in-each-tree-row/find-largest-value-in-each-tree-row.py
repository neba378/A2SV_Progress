# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return  []
        queue = deque([root])
        ans = [root.val]
        while queue:
            l = len(queue)
            m = float("-inf")
            for i in range(l):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    m = max(m,node.left.val)
                if node.right:
                    queue.append(node.right)
                    m = max(m,node.right.val)
            ans.append(m)
        ans.pop()
        return ans
            
                

