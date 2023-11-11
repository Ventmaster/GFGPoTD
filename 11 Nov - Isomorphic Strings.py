# 11 November 2023
# Isomorphic Strings

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1) != len(str2):
            return 0
            
        mapping = {}
        
        for char1, char2 in zip(str1, str2):
            if char1 in mapping:
                if mapping[char1] != char2:
                    return 0
            else:
                if char2 in mapping.values():
                    return False
                
                mapping[char1] = char2
                
        return 1
