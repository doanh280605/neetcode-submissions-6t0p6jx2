class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        res = 0 
        l = 0

        for r in range(len(s)): 
            while s[r] in table: 
                table.remove(s[l])
                l += 1
            table.add(s[r])
            res = max(res, r - l + 1)
        
        return res