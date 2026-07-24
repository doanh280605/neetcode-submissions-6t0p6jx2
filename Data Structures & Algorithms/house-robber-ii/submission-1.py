class Solution:
    def rob(self, nums: List[int]) -> int:
        def dep(arr): 
            n = len(arr)
            dp = [0] * (n + 1)

            if n == 0: 
                return 0 
            
            if n == 1: 
                return arr[0]

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n): 
                skip = dp[i - 1]
                rob = dp[i - 2] + arr[i]
                dp[i] = max(skip, rob)
            
            return dp[n - 1]
        
        return max(dep(nums[:-1]), dep(nums[1:]))