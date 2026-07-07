"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create a hash table to store the node's copy 
        hash = {} 

        def dfs(node): 
            if not node: 
                return None
            
            # if node in table, return copy of that node
            if node in hash: 
                return hash[node]
            
            # else create copy and add it to the table 
            copy = Node(node.val)
            hash[node] = copy 

            # after create the copy, loop through the node neighbors
            # to create the copy for the neighbors then append it to the 
            # table 
            for n in node.neighbors: 
                clone = dfs(n)
                
                # the neighbor will return the copy of its self
                # so we will append the current node copy to the neighbor
                # copy
                # node -> neighbors
                # copy -> clone (connect these two)
                copy.neighbors.append(clone)
            
            return copy # return copy for the next neighbors to append
        
        return dfs(node)

            
