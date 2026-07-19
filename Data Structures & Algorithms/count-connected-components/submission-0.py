class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set() 

        graph = {i : [] for i in range(n)}
        for a, b in edges: 
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node): 
            visit.add(node)

            for next in graph[node]: 
                if next not in visit: 
                    dfs(next)
                # no return because after looking at the
                # first neighbor the func immediately return 
                # no return so when for loop finishes naturally, 
                # python return automatically 
        
        count = 0 
        for node in range(n): 
            if node in visit: 
                continue
            if node not in visit: 
                dfs(node)
                count += 1
        
        return count