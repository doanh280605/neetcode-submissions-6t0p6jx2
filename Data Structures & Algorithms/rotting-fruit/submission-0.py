class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque() 
        counter = 0 

        for r in range(row): 
            for c in range(col): 
                if grid[r][c] == 2: 
                    q.append((r, c))
                if grid[r][c] == 1: 
                    counter += 1
        
        
        minute = 0 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q and counter > 0: 
            for i in range(len(q)): # it represents every thing happen in 1 minute
                r, c = q.popleft() 

                for dr, dc in directions: # explore the neighbor for this rotten tomatoes
                    nr, nc = r + dr, c + dc 

                    if (0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1): 
                        grid[nr][nc] = 2 # for this 1 minute, make fresh to rotten 
                        counter -= 1 # deduct the amount of fresh 
                        q.append((nr, nc)) # and add this rotten one to the queue
            
            minute += 1
        
        return minute if counter == 0 else -1 
