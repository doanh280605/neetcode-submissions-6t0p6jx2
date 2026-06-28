class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        path = [] 

        # create backtrack function take index and cur sum as param 
        def backtrack(i, total): 
            # if total = target return and append 1 valid path 
            if total == target: 
                res.append(path[:])
                return
            
            if i >= len(nums) or total > target: 
                return # safe guard function 

            # if those two if didnt return 
            # which mean the condition still valid
            # append current number to path 
            path.append(nums[i])

            # since each number can be use indefinite time 
            # call the backtrack function on the same current value 
            # check if the new sum satisfied 
            backtrack(i, total + nums[i])
            path.pop()

            # if not, call the backtrack function on the new value in
            # num array 
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return res