class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}

        if len(s) != len(t): 
            return False
        
        for char in s: 
            if char in charMap: 
                charMap[char] += 1
            else: 
                charMap[char] = 1

        for char in t: 
            if char in charMap: 
                charMap[char] -= 1
            else: 
                return False 

        for key in charMap.keys():
            if charMap[key] != 0:
                return False

        return True
        