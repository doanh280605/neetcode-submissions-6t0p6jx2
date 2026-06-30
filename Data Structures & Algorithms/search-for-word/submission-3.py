class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        def backtrack(r, c, counter): 
            if counter == len(word): 
                return True
            
            if (min(r, c) < 0 or 
                r >= row or c >= col or
                (r, c) in path or 
                board[r][c] != word[counter]): 
                return False
            
            path.add((r, c))
            res = (backtrack(r + 1, c, counter + 1) or 
                    backtrack(r - 1, c, counter + 1) or 
                    backtrack(r, c + 1, counter + 1) or 
                    backtrack(r, c - 1, counter + 1))
            path.remove((r, c))
            
            return res
        
        for r in range(row): 
            for c in range(row): 
                if backtrack(r, c, 0): 
                    return True
        
        return False