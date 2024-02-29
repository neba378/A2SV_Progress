# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        hash = defaultdict(list)
        def traverse(row,col,root):
            
            lst.append([col,row,root.val])

            if root.left:
                traverse(row+1,col-1,root.left)
            if root.right:
                traverse(row+1,col+1,root.right)
            return
        traverse(0,0,root)
        lst.sort(key=lambda x: (x[0],x[1],x[2]))
        for i in lst:
            hash[i[0]].append(i[2])
        ans = []
        for i in hash:
            ans.append(hash[i])
        return ans
        