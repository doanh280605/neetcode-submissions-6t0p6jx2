class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {} 

        for num in nums: 
            table[num] = 1 + table.get(num, 0)
        
        arr = []
        for num, cnt in table.items(): 
            arr.append([cnt, num])
        
        arr.sort() 

        res = [] 
        while len(res) < k: 
            res.append(arr.pop()[1])