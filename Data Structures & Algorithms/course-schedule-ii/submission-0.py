class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path, visit = set(), set() 

        graph = {i : [] for i in range(numCourses)}
        
        for course, pre in prerequisites: 
            graph[pre].append(course)
        
        def dfs(node): 
            if node in path: 
                return False
            
            if node in visit: 
                return True
            
            path.add(node)
            
            for nxt in graph[node]:
                if not dfs(nxt): 
                    return False
            
            path.remove(node)
            visit.add(node)
            return True
        
        for c in range(numCourses): 
            if not dfs(c): 
                return []
        
        return list(visit)