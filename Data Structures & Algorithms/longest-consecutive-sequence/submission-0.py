class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() 

        counter = 0 

        for i in range(len(nums)): 
            if nums[i] + 1 == nums[i + 1]: 
                counter += 1
        
        return counter