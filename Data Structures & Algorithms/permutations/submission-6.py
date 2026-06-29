class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        path = [] 
        check = set() 

        def backtrack(i): 
            if len(path) == len(nums):
                res.append(path[:])
                return # you are done when you have a complete permutation
                # there is nothing left to explore from this state
                # so thats why you return
            
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