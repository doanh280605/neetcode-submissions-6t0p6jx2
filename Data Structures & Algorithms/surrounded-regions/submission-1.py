class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # the idea is that traverse the border of the board
        # mark all O in the side as T
        # then any that we can reach from that T will not gonna be converted
        # any O that cant be reach from the border will be X
        row, col = len(board), len(board[0])

        def dfs(r, c): 
            if (r < 0 or r == row or
                c < 0 or c == col or
                board[r][c] != "O"): 
                return 
            # we want to mark border O and its O neighbor as T so we wont accidentally change them to X
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # traverse the border of the board and start traversing O neighbor
        for r in range(row): 
            for c in range(col): 
                if (board[r][c] == "O" and 
                    (r in [0, row - 1] or c in [0, col - 1])):
                    dfs(r, c)
        
        for r in range(row): 
            for c in range(col): 
                if board[r][c] == "O": 
                    board[r][c] = "X"
        
        for r in range(row): 
            for c in range(col): 
                if board[r][c] == "T": 
                    board[r][c] = "O"
