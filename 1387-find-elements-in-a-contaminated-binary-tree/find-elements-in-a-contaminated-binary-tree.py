# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:


    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.s = {0}
        self.build(root, self.s)
        
        
    def build(self, root, s):
        if not root:
            return
        if root.left:
            root.left.val = root.val*2+1
            s.add(root.val*2+1)
            self.build(root.left, s)
        if root.right:
            root.right.val = root.val*2+2
            s.add(root.val*2+2)
            self.build(root.right, s)

    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)