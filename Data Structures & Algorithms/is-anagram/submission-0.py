class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set(s) 
        
        for c in t: 
            if c in seen: 
                return True
        
        return False