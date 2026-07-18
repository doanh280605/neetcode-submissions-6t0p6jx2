class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path, visit = set(), set() 
        order = [] 

        graph = {i : [] for i in range(numCourses)}

        for course, pre in prerequisites: 
            graph[pre].append(course)
        
        def dfs(node): 
            if node in path: 
                return False
            
            if node in visit: 
                return True
            
            path.add(node)

            for next in graph[node]: 
                if not dfs(next): 
                    return False
            
            path.remove(node)
            visit.add(node)
            order.append(node)
            return True
        
        for i in range(numCourses): 
            if not dfs(i): 
                return []
        
        return order[::-1]