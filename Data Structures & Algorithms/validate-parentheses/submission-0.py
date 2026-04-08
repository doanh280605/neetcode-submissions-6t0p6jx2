class Solution:
    def isValid(self, s: str) -> bool:
        stack = {")":"(", "]":"[", "}":"{"}
        res = [] 

        for c in s: 
            if c in res: 
                if res and res[-1] == stack[c]: 
                    res.pop() 
                else: 
                    return False
            else: 
                res.append(c)
        
        return True if res else False