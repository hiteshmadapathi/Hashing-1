# Time Complexity --> O(n*k) where n is the max length of array and k is the average size of each string within the array
# Space Complexity --> O(n)
# Approach --> Assigning prime numbers to each of the lower case alphabet and then calcualting the value of each string by doing a product of prime number, we arrive at a unique way of having same value
# for all the anagrams. Then utilizing the hashmap to store all the anagrams corresponding to a particular value in an array.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def CalcValue(string):
            primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,67,71,73,79,83,89,97,101,103]
            output = 1
            for i in range(len(string)):
                output = output*primes[ord(string[i])-ord('a')]
            return output

        hmap = {} 
        for string in strs:
            value = CalcValue(string) 
            if value not in hmap: 
                hmap[value] = [] 
            hmap[value].append(string)
        
        return list(hmap.values())
