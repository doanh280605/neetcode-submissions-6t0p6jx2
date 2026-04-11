class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() 
        print("List sort: ", nums) 

        counter = 0 

        for i in range(1, len(nums)): 
            print("Num i", nums[i])
            print("Num i - 1", nums[i - 1])
            if nums[i] == nums[i - 1]: 
                counter += 1
        
        return counter