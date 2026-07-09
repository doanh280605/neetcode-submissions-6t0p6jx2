class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacific, atlantic = set(), set() 
        res = [] 

        def dfs(r, c, prevHeight, visit): 
            if (
                r < 0 or r >= row or
                c < 0 or c >= col or
                (r, c) in visit or
                heights[r][c] < prevHeight
            ):
                return
            
            visit.add((r, c))

            dfs(r - 1, c, heights[r][c], visit)
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
        
        for c in range(col): 
            dfs(0, c, heights[0][c], pacific)
        
        for r in range(row): 
            dfs(r, 0, heights[r][0], pacific)
        
        for c in range(col): 
            dfs(row - 1, c, heights[row - 1][c], atlantic)
        
        for r in range(row): 
            dfs(r, col - 1, heights[r][col - 1], atlantic)

        for r in range(row): 
            for c in range(col): 
                if (r, c) in pacific and (r, c) in atlantic: 
                    res.append([r, c])
        
        return res

