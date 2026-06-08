# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        
        def dfs(root, maxv): 
            if not root: 
                return 0 
            maxv = max(maxv, root.val)
            left = dfs(root.left, maxv)
            right = dfs(root.right, maxv)

            if root.val >= maxv: 
                res.append(root.val)
        
        dfs(root, float('-inf'))
        return len(res)
