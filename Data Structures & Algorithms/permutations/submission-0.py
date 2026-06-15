class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        path = [] 
        check = set()

        def backtrack(): 
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)): 
                if nums[i] in check: 
                    continue
                
                if nums[i] not in check:
                    path.append(nums[i])
                    check.add(nums[i])
                backtrack()
                path.pop() 
                check.remove(nums[i])
            
        backtrack()
        return res