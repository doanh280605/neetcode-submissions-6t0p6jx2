class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict() 

        for s in strs: 
            sort = ''.join(sorted(s))
            res[sort].append(s)
        
        return res
