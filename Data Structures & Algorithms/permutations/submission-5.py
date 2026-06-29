class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        path = [] 
        check = set() 

        def backtrack(i): 
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for i in range(len(nums)): 
                if nums[i] in check: 
                    continue

                path.append(nums[i])
                check.add(nums[i])
                backtrack(i + 1)
                check.remove(nums[i])
                path.pop()
        
        backtrack(0)
        return res