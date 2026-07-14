class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set() 
        finished = set()

        # first create an empty graph 
        graph = {i : [] for i in range(numCourses)}

        # fill in the connection
        for course, pre in prerequisites: 
            graph[pre].append(course)

        def dfs(cur): 
            if cur in path:
                return False 

            if cur in finished: 
                return True

            path.add(cur)

            for nxt in graph[cur]: 
                if not dfs(nxt):
                    return False 

            path.remove(cur)
            finished.add(cur)
            return True
        
        for c in range(numCourses): 
            if not dfs(c): 
                return False
        
        return True