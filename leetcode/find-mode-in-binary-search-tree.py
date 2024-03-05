# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()
        maxi = -100001
        lst = []
        def traverse(node):
            nonlocal maxi
            if not node:
                return None
            
            counter[node.val]+=1
            maxi = max(maxi,counter[node.val])
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(root)
        for i,j in counter.items():
            if j == maxi:
                lst.append(i)
        return(lst)