class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 

        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        arr = [] 
        for num, count in count.items: 
            arr.append([count, num])
        arr.sort() 

        res = [] 

        while len(res) < k: 
            res.append(count.pop()[1])
        
        return res