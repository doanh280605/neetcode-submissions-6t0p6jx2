class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = [] 
        check = set() 

        def backtrack(i): 
            subset = tuple(sorted(path))

            if subset not in check: 
                res.append(path[:])
                check.add(subset) 
                # no return because every node is a valid answer
                # but if you return then you will never continue extending
                # the subset
            
            for i in range(i, len(nums)): 
                path.append(nums[i])
                backtrack(i + 1)
                path.pop() 
        
        backtrack(0)
        return res

