# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        def rec(node,now,tot):
            nonlocal ans
            if not now:
                return
            if tot+now.val==targetSum:
                ans+=1
            rec(node,now.left,tot+now.val)
            rec(node,now.right,tot+now.val)
            
        def findPath(node):
            if not node:
                return
            rec(node,node,0)
            findPath(node.left)
            findPath(node.right)
            
        findPath(root)
        return(ans)
            
            
'''
0
5
9
20
0
4
15
4 7
15
17
17
4
0
8
21
21
8
12
17
17
12
13
13
20
5 2
9
5
13
0
4
15
4 7
15
17
17
4
0
8
21
21
8
12
17
17
12
13
13
13
17
5 5
17
18
18
'''