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

            if node in finished: 
                return True

            path.add(cur)
