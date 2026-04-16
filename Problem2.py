# Time Complexity --> O(n)
# Space Complexity --> O(1)
# Approach --> Using 2 hashmaps to kepp track of mappings from 1 string to the other. If there is a conflixt then return False, else True. 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        smap = {}
        tmap = {}

        for i in range(len(s)):
            if s[i] in smap and smap[s[i]]!=t[i]:
                return False
            if t[i] in tmap and tmap[t[i]]!=s[i]:
                return False
            smap[s[i]] = t[i]
            tmap[t[i]] = s[i]
        return True 
        
