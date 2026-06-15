class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        path = [] 
        check = set()

        def backtrack(): 
            if len(path) == len(nums): 
                res.append(path[:])
                return 
            
            for num in nums: 
                if num in check: 
                    continue
                
                path.append(num)
                check.add(num)
                backtrack() 
                path.pop()
                check.remove(num)
        backtrack()
        return res