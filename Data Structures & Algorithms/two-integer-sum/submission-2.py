class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {} 

        for i, num in enumerate(nums): 
            if target - num in table: 
                return [table[target-num], i] # we return the index
            table[num] = i # we store the number with key as index position 
        
        return []