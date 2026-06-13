class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        path = []

        def backtrack(start): 
            total = 0
            while start < len(nums): 
                total += nums[start]
                path.append(nums)

                if total == target: 
                    res.append(path)
                else: 
                    backtrack(start + 1)
        backtrack(0)
        return res