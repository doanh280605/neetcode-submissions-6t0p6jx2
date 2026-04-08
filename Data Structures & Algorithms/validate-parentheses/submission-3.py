class Solution:
    def isValid(self, s: str) -> bool:
        stack =  { ")" : "(", "]" : "[", "}" : "{" }
        res = [] 

        for c in s: 
            if c in stack: 
                if res and res[-1] == stack[c]: 
                    res.pop() 
                else: 
                    return False
            else: 
                res.append(c)
        
        return True if not res else False