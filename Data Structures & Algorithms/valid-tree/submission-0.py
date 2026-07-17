class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()

        if len(edges) != n - 1: 
            return False
        
        graph = {i : [] for i in range(n)}
        
        # because this is a undirected graph
        # the graph construction should be different
        for a, b in edges: 
            graph[a].append(b)
            graph[b].append(a)


        def dfs(node, parent): 
            visit.add(node)

            for next in graph[node]: 
                if next == parent: 
                    continue
                
                if next in visit: 
                    return False
                
                if not dfs(next, node): 
                    return False
            return True
        
        # of course the root doesnt have a parent, leave it as -1
        if not dfs(0, -1): 
            return False
        
        return len(visit) == n