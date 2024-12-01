# 01st December 2024
# Non Repeating Character

class Solution:
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        d = [0 for i in range(26)]
        
        for i in s:
            d[ord(i) - ord('a')] += 1
            
        for i in s:
            if d[ord(i) - ord('a')] == 1:
                return i
                
        return '$'
