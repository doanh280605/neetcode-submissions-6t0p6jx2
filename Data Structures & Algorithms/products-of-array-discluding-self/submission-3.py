class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [], []
        l, r = 1, 1 

        res = [] 

        for i in range(len(nums)): 
            left.append(l)
            l *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1): 
            right.append(r)
            r *= nums[i]
        
        right.reverse() 

        for i in range(len(nums)): 
            res.append(left[i] * right[i])
        
        return res
