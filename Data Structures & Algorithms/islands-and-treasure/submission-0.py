class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        q = deque()

        directions = [
            [1, 0], 
            [-1, 0], 
            [0, 1], 
            [0, -1]
        ]

        # put all treasure into the queue
        for r in range(row): 
            for c in range(col): 
                if grid[r][c] == 0: 
                    q.append((r, c))
        
        # while queue is not empty 
        while q: 
            r, c = q.popleft() # take one cell
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc # look at its 4 neighbors
                
                if nr < 0 or nr >= row or nc < 0 or nc >= col:
                    continue

                if grid[nr][nc] == 2147483647: 
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
        