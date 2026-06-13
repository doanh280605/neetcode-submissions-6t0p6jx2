class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        path = []

        def backtrack(start, total): 
            if total == target: 
                res.append(path[:])
                return 
            
            if start == len(nums) or total > target: 
                return 
            
            path.append(nums[start])
            backtrack(start, total + nums[start])
            path.pop()

            backtrack(start + 1, total) 


        backtrack(0, 0)
        return res