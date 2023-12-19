# 19 December 2023
# Rightmost different bit 

class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        result = m ^ n 
        
        if result == 0:
            return -1 
            
        pos = 1
        while result:
            if result & 1:
                return pos
            result >>= 1
            pos += 1
        
        return result 
