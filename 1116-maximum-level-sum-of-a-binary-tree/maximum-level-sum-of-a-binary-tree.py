# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maxi = root.val
        ans = 1
        level = 1
        while queue:
            lst = []
            level+=1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    lst.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    lst.append(node.right.val)
            s = sum(lst)
            if lst!=[] and s>maxi:
                maxi = s
                ans = level 
        return ans
            
            
