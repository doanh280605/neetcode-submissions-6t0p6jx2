class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        maxWater = 0 

        while l < r: 
            if l < r: 
                print("left: ", heights[l])
                print("right: ", heights[r])
                print("lenght", r - l)
                print("area", (heights[r] - heights[l]) * (r - l) )
                maxWater = max(maxWater, ((heights[r] - heights[l]) * l))
                l += 1
            else: 
                print("left: ", l)
                print("right: ", r)
                print("maxWater: ", maxWater )
                maxWater = max(maxWater, (heights[l] - heights[r]) * r)
                r -= 1
        
        return maxWater
