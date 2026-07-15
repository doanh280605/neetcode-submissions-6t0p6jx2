class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # a set to track current node and a set to track visited node
        path = set() 
        visit = set()
        # first create an empty graph 
        graph = {i : [] for i in range(numCourses)}
        # fill in the connection
        for course, pre in prerequisites: 
            graph[pre].append(course)

        # if a node is in cur set, which mean we detect a cycle 
        # because we are traversing the node pre and if we see that node again, it hasnt done traversing yet 
        # met again meaning that there is a cycle, return False
        # if its child node all return True, the node itself is not a cycle, remove from the cur set and add to finish set
        # return True
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
        
        for i in range(numCourses): 
            if not dfs(i): 
                return False
        
        return True