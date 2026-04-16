# Time Complexity --> O(n)
# Space Complexity --> O(1)
# Approach --> Converting the s to a list of strings and then using 2 hashmaps to keep track of mappings from pattern to the sList. If there is a conflixt then return False, else True. 
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split()
        if len(pattern)!=len(sList):
            return False
        
        pmap = {}
        smap = {}
        for i in range(len(pattern)):
            if pattern[i] in pmap and pmap[pattern[i]]!=sList[i]:
                return False
            if sList[i] in smap and smap[sList[i]]!=pattern[i]:
                return False
            pmap[pattern[i]] = sList[i]
            smap[sList[i]] = pattern[i]
            
        return True 
