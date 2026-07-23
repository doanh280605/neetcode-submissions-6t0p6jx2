class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(n): 
            skip = dp[i - 1] # if we choose to skip the current house
            # what is the best value up to house i - 1? 

            # but if we choose to rob the current house
            # what is the best value up to house i - 2 (not adjacent house) + this cur house?
            rob = dp[i - 2] + nums[i]

            dp[i] = max(skip, rob) # then pick between them which path is better to go, skip or rob
        
        return dp[n]