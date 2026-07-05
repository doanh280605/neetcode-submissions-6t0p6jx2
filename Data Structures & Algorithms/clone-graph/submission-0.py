"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        check = {} 

        def dfs(node): 
            if not node:
                return None

            if node in check: 
                return check[node]

            copy = Node(node.val)

            check[node] = copy 

            for neighbor in node.neighbors: 
                clone = dfs(neighbor)

                copy.neighbors.append(clone)
            return copy 

        return dfs(node)
            
