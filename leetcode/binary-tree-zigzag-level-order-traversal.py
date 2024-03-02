# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root]) if root else deque()
        re = deque([root.val]) if root else deque()
        res = []
        flag = 1
        while queue:
            if flag == 1:
                temp = re.copy()
                
            else:
                re.reverse()
                temp = re.copy()
            flag = 1-flag
            res.append(temp)
            
            for _ in range(len(queue)):
                node = queue.popleft()
                re.popleft()
                if node.left:
                    queue.append(node.left)
                    re.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    re.append(node.right.val)
        return res
            
