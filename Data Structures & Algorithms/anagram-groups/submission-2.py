class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs: 
            sort = ''.join(sorted(s))
            res[s].append(sort)
        
        return list(res.values())