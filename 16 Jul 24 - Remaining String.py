# 16 July 2024
# Remaining String

class Solution:
    def printString(self, s, ch, count):
        # code here
        index = -1
        
        for i in range(len(s)):
            if s[i] == ch and count > 0:
                index = i
                count -= 1
                
        if index == -1 or count > 0:
            return ""
            
        return s[index + 1:]
