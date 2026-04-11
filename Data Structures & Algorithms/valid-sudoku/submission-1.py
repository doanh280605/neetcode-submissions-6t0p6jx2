class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        square = defaultdict(list)

        for r in range(len(row)): 
            for c in range(len(col)): 
                if board[r][c] == ".": 
                    continue 
                
                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or 
                    board[r][c] in square[(r // 3, c // 3)]): 
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
            
        
        return True