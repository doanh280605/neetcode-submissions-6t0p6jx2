# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        queue = deque([(root, float('-inf'))])

        while queue:
            node, maxsf = queue.popleft() 
            
            if node: 
                if node.val >= maxsf: 
                    res.append(node.val)
                    maxsf = max(node.val, maxsf)
                else: 
                    maxsf = max(maxsf, node.val)
            else: 
                continue
            
            queue.append((node.left, maxsf))
            queue.append((node.right, maxsf))
        
        return len(res)