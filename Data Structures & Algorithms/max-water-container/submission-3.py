class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        res = 0 

        for l in range(len(heights)): 
            area = min(heights[l], heights[r]) * (r - l)

            res = max(area, res)

            if heights[l] <= heights[r]: 
                l += 1
            else: 
                r -= 1
        return res
