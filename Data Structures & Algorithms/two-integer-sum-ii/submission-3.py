class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {} 

        for i, num in enumerate(numbers): 
            if target - num in table: 
                return [table[target - num], i]
            
            table[num] = i
        return []