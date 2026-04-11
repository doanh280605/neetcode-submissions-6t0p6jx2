class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = []
        left_total = 1
        right = [] 
        right_total = 1

        res = []

        for i in range(len(nums)): 
            left_total *= nums[i + 1]
            left.append(left_total)
        
        for i in range(len(nums) - 1, -1, -1):
            right_total *= nums[i]
            right.append(right_total)
        
        for i in range(len(left_total)): 
            res.append(left_total[i] * right_total[i])
        
        return res
