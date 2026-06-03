# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # a queue needs two operations: add to the back and remove from the front
        # which is the purpose of deque: double-ended queue
        queue = deque([root])
        result = []

        while queue: 
            level = [] 

            for i in range(len(queue)): 
                node = queue.popleft() # remove from the front

                if not node: 
                    return result

                level.append(node.val)

                if node.left:
                    queue.append(node.left) # add to the back
                
                if node.right: 
                    queue.append(node.right)
                
            result.append(level)
        
        return result