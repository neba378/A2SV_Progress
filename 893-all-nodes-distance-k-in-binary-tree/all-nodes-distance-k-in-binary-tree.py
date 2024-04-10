# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue = deque([root])
        dic = defaultdict(list)
        ans = []
        if not root:
            return []
        while(queue):
            
            for _ in range(len(queue)):
                inter = []
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    dic[node.val].append(node.left.val)
                    dic[node.left.val].append(node.val)
                if node.right:
                    queue.append(node.right)
                    dic[node.val].append(node.right.val)
                    dic[node.right.val].append(node.val)
        queue = deque([target.val])
        visited = set()
        while k>0 and queue:
            for i in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                for j in dic[node]:
                    if j not in visited:
                        queue.append(j)
                        
            k-=1
        ans.extend(queue)
        return ans