import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float('inf')

        if not piles: 
            return 0

        while l <= r: 
            time = 0
            mid = (l + r) // 2 # 2

            for p in piles: 
                time += math.ceil(p / mid)
                # 3 + mid 
            
            if time <= h: 
                res = min(res, mid)
                r = mid - 1
            elif time > h:
                l = mid + 1
        
        return int(res) 
