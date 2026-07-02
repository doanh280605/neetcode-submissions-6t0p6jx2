class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set() 
        land = 0

        def dfs(r, c): 
            if r < 0 or r >= row or c < 0 or c >= col: 
                return
            
            if grid[r][c] == "0": 
                return 
            
            if (r, c) in visited: 
                return 
                
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
            
        for r in range(row): 
            for c in range(col): 
                if grid[r][c] == "1" and (r, c) not in visited: 
                    land += 1
                    dfs(r, c)

        
        return land
