# 01 February 2024
# Panagram Checking

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        charSet = set()
        
        for i in s.lower():
            if i.isalpha():
                charSet.add(i)
        
        if len(charSet) == 26:
            return 1
        else:
            return 0
