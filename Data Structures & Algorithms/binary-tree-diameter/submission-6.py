# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# first, create global value
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 

        def dfs(cur): 
            if not cur: 
                return 0
            
            left, right = dfs(cur.left), dfs(cur.right)

            # res = max height of the left subtree and the right subtree
            self.res = max(self.res, left + right)

            # return the height of each root, by comparing the height of left and right
            # then take the max and + 1 for itself
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
        