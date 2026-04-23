class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r: 
            mid = l + (r - l) // 2

            if nums[mid] < nums[r] and target > nums[mid]: 
                r = mid - 1
            elif nums[mid] > nums[l] and target < nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1