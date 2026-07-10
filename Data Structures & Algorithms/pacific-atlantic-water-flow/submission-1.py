class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # use set to record cells that can reach that ocean 
        # normal dfs approach 
        # after DFS, take intersection of two sea and return 
        # reverse the seach: pacific => find every cell that can reach it 
        row, col = len(heights), len(heights[0])
        res = [] 
        pacific, atlantic = set(), set()

        def dfs(r, c, prevHeight, visit): 
            if (r < 0 or r >= row or 
                c < 0 or c >= col or 
                heights[r][c] < prevHeight or
                (r, c) in visit): 
                return 
            
            visit.add((r, c))

            dfs(r + 1, c, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
        
        for r in range(row): 
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, col - 1, heights[r][col - 1], atlantic)

        for c in range(col): 
            dfs(0, c, heights[0][c], pacific)
            dfs(row - 1, c, heights[row - 1][c], atlantic)
        
        for r in range(row): 
            for c in range(col): 
                if (r, c) in pacific and (r, c) in atlantic: 
                    res.append([r, c])
        
        return res