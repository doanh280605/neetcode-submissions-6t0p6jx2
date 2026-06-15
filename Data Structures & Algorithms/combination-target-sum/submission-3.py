class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = [] 

        def backtrack(x, total): 
            if total == target:
                res.append(path[:])
                return 
            
            if x == len(nums) or total> target: 
                return 
            
            path.append(nums[x])
            backtrack(x, total + nums[x])
            path.pop() 

            backtrack(x + 1, total)
        
        backtrack(0, 0)
        return res