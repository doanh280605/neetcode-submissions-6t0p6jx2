# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root): 
            if not root: 
                return [True, 0]
                
            left, right = dfs(root.left), dfs(root.right)

            # if left is balance and right is balance and left - right is not more than 1
            # balance is true
            # store the balance state of left and right
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # store the max height of that root by compare left and right + 1 itself
            # like previouos problem 
            return [balance, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]