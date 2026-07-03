class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        maxLand = 0 
        visit = set()

        def dfs(r, c): 
            if r < 0 or r >= row or c < 0 or c >= col: 
                return 0
            
            if grid[r][c] == 0: 
                return 0
            
            if (r, c) in visit: 
                return 0
            
            visit.add((r, c))

            return (1 + dfs(r + 1, c)
                    + dfs(r - 1, c)
                    + dfs(r, c + 1)
                    + dfs(r, c - 1))
        
        for r in range(row): 
            for c in range(col): 
                if (r, c) not in visit and grid[r][c] == 1: 
                    area = dfs(r, c)
                    maxLand = max(maxLand, area)
        
        return maxLand
            
