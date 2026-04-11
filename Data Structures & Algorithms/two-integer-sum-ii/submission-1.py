class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {} 

        for i, num in enumerate(numbers): 
            if target - num in table: 
                return [table[num] + 1, i + 1]
            
            table[num] = i
        return []