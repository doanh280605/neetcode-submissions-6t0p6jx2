class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        table = set() 

        for n in nums: 
            if n in table: 
                return n
            
            table.add(n)
        
        return -1