# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        queue = deque([root])

        while queue:
            big = root.val

            for i in range(len(queue)): 
                node = queue.popleft() 
                
                if node: 
                    if node.val >= big: 
                        res.append(node.val)
                    else: 
                        big = max(big, node.val)
                else: 
                    continue
                
                queue.append(node.left)
                queue.append(node.right)
        
        return len(res)