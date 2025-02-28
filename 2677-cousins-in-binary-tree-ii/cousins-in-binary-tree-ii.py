# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        queue = deque([[root,None]])
        ans = []
        while queue:
            n = len(queue)
            for i in range(n):
                node,idx = queue.popleft()
                if node.left:
                    queue.append([node.left,node])
                if node.right:
                    queue.append([node.right,node])
            if queue:
                ans.append([nod for nod in queue])
        dic = {}
        for nodes in ans:
            s = sum([nod.val for nod,idx in nodes])
            for i in range(len(nodes)):
                temp = s
                if i>0:
                    if nodes[i][1] == nodes[i-1][1]:
                        temp-=nodes[i-1][0].val
                if i<len(nodes)-1:
                    if nodes[i+1][1] == nodes[i][1]:
                        temp-=nodes[i+1][0].val
                temp -= nodes[i][0].val
                dic[nodes[i][0]] = temp
        for k,v in dic.items():
            k.val  = v
        root.val = 0
        return root
        
            

                