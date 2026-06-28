class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        path = [] 
        candidates.sort() 

        def backtrack(i, total): 
            if total == target: 
                res.append(path[:])
                return 
            
            if i >= len(candidates) or total > target: 
                return 
            
            for x in range(i, len(candidates)): 
                if x > i and candidates[x] == candidates[x - 1]: 
                    continue
                
                path.append(candidates[x])
                backtrack(x + 1, total + candidates[x])
                path.pop() 
        backtrack(0,0)
        return res