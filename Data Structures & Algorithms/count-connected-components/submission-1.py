class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set() 

        graph = {i : [] for i in range(n)}
        
        for a, b in edges: 
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node): 
            for nxt in graph[node]:
                if nxt not in visit: 
                    visit.add(nxt)
                    dfs(nxt)

        count = 0 

        for node in range(n): 
            if node not in visit: 
                dfs(node)
                count += 1
        
        return count