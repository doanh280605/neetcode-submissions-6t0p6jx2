class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = []
        left_total = 1
        right = [] 
        right_total = 1

        res = []

        for i in range(len(nums)): 
            left.append(left_total)
            left_total *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            right.append(right_total)
            right_total *= nums[i]
        
        right.reverse()

        for i in range(len(left_total)): 
            res.append(left[i] * right[i])
        
        return res
