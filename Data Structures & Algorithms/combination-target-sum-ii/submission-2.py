class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        path = [] 
        candidates.sort() # sort so that we can identify when to skip 

        def backtrack(i, total): 
            # the same as previous question
            if total == target: 
                res.append(path[:])
                return 
            
            if i >= len(candidates) or total > target: 
                return 
            
            # use a x pointer to loop inside the range i
            # as a sliding window because we want to identify where is the 
            # start for the new combinations
            for x in range(i, len(candidates)): 
                # so if x is not the beginning of the range 
                # and there is a duplicate, meaning that we want to skip 
                # exploring this "branch" because two same number will 
                # give two same combinations, so if the next num is same
                # as the prev one we skip 
                if x > i and candidates[x] == candidates[x - 1]: 
                    continue
                
                path.append(candidates[x])
                # continue checking in that range
                backtrack(x + 1, total + candidates[x])
                path.pop() 
        backtrack(0,0)
        return res