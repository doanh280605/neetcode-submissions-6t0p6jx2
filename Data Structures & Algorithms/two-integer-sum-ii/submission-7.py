class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {} 
        res = [] 

        for i, num in enumerate(numbers): 
            if target - num in table: 
                res.append([table[target - num], i])
            
            table[num] = i
        return res